from rich.console import Console # For console output (i.e., colors, emojis, etc.)
from rich.panel import Panel
from player import Player
from quest import Quest

console = Console()

class Main:
    def __init__(self):
        console.print(Panel.fit("Greetings, Chosen Undead :skull:!", title=":fire: SoulKeeper :fire:", style="gold1"))
        self.start = True
        self.access = False

    def start_app(self):
        # Prompt the user to enter a valid name and starting number of souls before proceeding
        while self.start:
            self.player_name = console.input("Please enter your name: ").strip()

            if not self.player_name:
                print("You must enter a name.\n")
                continue

            try:
                self.player_souls = int(console.input("Enter how many souls :fire: you have: "))
                if self.player_souls < 0:
                    print("Souls must be a positive integer.\n")
                    continue
                self.start = False 
            except ValueError:
                print("You must enter a valid integer for souls.\n")

    def create_quests(self,player):
        quests = [
            # General Quests
            Quest(
                name="First Steps",
                description="Level up for the first time choosing any attribute.",
                requirements={("selected_class", "Level"): 1},
                rewards={"total_souls": 10000}
            ),

            # Attribute Leveling Quests
            Quest(
                name="Vitality Boosting",
                description="Level up Vitality to 50.",
                requirements={("selected_class", "Vitality"): 50},
                rewards={"total_souls": 50000}
            ),

            Quest(
                name="Attunement Studying",
                description="Level up Attunement to 50.",
                requirements={("selected_class", "Attunement"): 50},
                rewards={"total_souls": 50000}
            ),

            Quest(
                name="Endurance Workout",
                description="Level up Endurance to 40.",
                requirements={("selected_class", "Endurance"): 40},
                rewards={"total_souls": 30000}
            ),

            Quest(
                name="Strength Training",
                description="Level up Strength to 50.",
                requirements={("selected_class", "Strength"): 40},
                rewards={"total_souls": 50000}
            ),

            Quest(
                name="Dexterity Training",
                description="Level up Dexterity to 45.",
                requirements={("selected_class", "Dexterity"): 45},
                rewards={"total_souls": 50000}
            ),

            Quest(
                name="Resistance Buffing",
                description="Level up Resistance to 30.",
                requirements={("selected_class", "Resistance"): 30},
                rewards={"total_souls": 50000}
            ),

            Quest(
                name="Intelligence Studying",
                description="Level up Intelligence to 50.",
                requirements={("selected_class", "Intelligence"): 50},
                rewards={"total_souls": 50000}
            ),

            Quest(
                name="Faith Pilgrimage",
                description="Level up Faith to 50.",
                requirements={("selected_class", "Faith"): 50},
                rewards={"total_souls": 50000}
            ),

            # Character Build Quests
            Quest(
                name="Path of the Warrior",
                description="Level up Warrior to 150.",
                requirements={"selected_class": "Warrior", ("selected_class", "Level"): 20},
                rewards={"total_souls": 100000}
            ),

            Quest(
                name="Path of the Warrior",
                description="Level up to 150 as a Warrior.",
                requirements={"selected_class": "Warrior", ("selected_class", "Level"): 150},
                rewards={"total_souls": 100000}
            ),

            Quest(
                name="Strength of the Knight",
                description="Level up to 150 as a Knight.",
                requirements={"selected_class": "Knight", ("selected_class", "Level"): 150},
                rewards={"total_souls": 100000}
            ),

            Quest(
                name="Endurance of the Wanderer",
                description="Level up to 150 as a Wanderer.",
                requirements={"selected_class": "Wanderer", ("selected_class", "Level"): 150},
                rewards={"total_souls": 100000}
            ),

            Quest(
                name="Agility of the Thief",
                description="Level up to 150 as a Thief.",
                requirements={"selected_class": "Thief", ("selected_class", "Level"): 150},
                rewards={"total_souls": 100000}
            ),

            Quest(
                name="Brutality of the Bandit",
                description="Level up to 150 as a Bandit.",
                requirements={"selected_class": "Bandit", ("selected_class", "Level"): 150},
                rewards={"total_souls": 100000}
            ),

            Quest(
                name="Patience of the Hunter",
                description="Level up to 150 as a Hunter.",
                requirements={"selected_class": "Hunter", ("selected_class", "Level"): 150},
                rewards={"total_souls": 100000}
            ),

            Quest(
                name="Talent of the Sorcerer",
                description="Level up to 150 as a Sorcerer.",
                requirements={"selected_class": "Sorcerer", ("selected_class", "Level"): 150},
                rewards={"total_souls": 100000}
            ),

            Quest(
                name="Power of the Pyromancer",
                description="Level up to 150 as a Pyromancer.",
                requirements={"selected_class": "Pyromancer", ("selected_class", "Level"): 150},
                rewards={"total_souls": 100000}
            ),

            Quest(
                name="Righteousness of the Cleric",
                description="Level up to 150 as a Cleric.",
                requirements={"selected_class": "Cleric", ("selected_class", "Level"): 150},
                rewards={"total_souls": 100000}
            ),

            Quest(
                name="Misery of the Deprived",
                description="Level up to 150 as a Deprived.",
                requirements={"selected_class": "Deprived", ("selected_class", "Level"): 150},
                rewards={"total_souls": 100000}
            )
        ]
        
        for quest in quests:
            player.add_quest(quest)

    def access_menu(self):
        # Grant user access to main menu 
        self.access = True
        self.player = Player(self.player_name, self.player_souls)
        self.create_quests(self.player)  # Assign quests to the player
        console.print(f"Welcome, {self.player_name}, to SoulKeeper! You start with {self.player_souls} souls :fire:!\n")
        self.choices()

    def menu(self):
        console.print("[dodger_blue1]1. Choose class :crossed_swords:")
        console.print("[green]2. Level up attribute :muscle:")
        console.print("[white]3. View current stats :scroll:")
        console.print("[turquoise2]4. Add more souls :heavy_plus_sign::fire:")
        console.print("[bright_magenta]5. Show spent souls :fire:")
        console.print("[purple]6. View quests :scroll:")
        console.print("[gold1]7. View achievements :trophy:")
        console.print("[bright_green]8. Save progress :file_folder:")
        console.print("[cyan]9. Load progress :unlock:")
        console.print("[bright_yellow]10. Delete progress :wastebasket:")
        console.print("[bright_red]11. Exit :coffin:\n")

    def menu_choice_1(self):
        if self.player.check_for_class == False:
            self.player.choose_class()
        else:
            console.print("You have already picked a class!\n")

    def menu_choice_2(self):
        if self.player.check_for_class == True:
            self.player.level_up()
        else:
            console.print("You must first choose a class before leveling up!\n")

    def menu_choice_3(self):
        if self.player.check_for_class == True:
            self.player.show_status()
        else:
            console.print("You must first choose a class before displaying your current status!\n")

    def menu_choice_4(self):
        try:
            self.more_souls = int(console.input("Enter how many souls :fire: you wish to add: "))
            self.player.add_souls(self.more_souls)
        except ValueError:
            console.print("You must enter a valid integer for souls.\n")

    def menu_choice_5(self):
        self.player.show_souls_spent()

    def menu_choice_6(self):
        self.player.show_quests()

    def menu_choice_7(self):
        self.player.view_achievements()

    def menu_choice_8(self):
        save = console.input(f"Do you wish to save your progress, {self.player_name}? Enter 'Y' for yes or 'N' for no. ")
        if save == "Y":
            self.player.save_progress()
        elif save == "N":
            console.print("Save canceled!\n")
        else:
            console.print("Invalid input!\n")

    def menu_choice_9(self):
        load = console.input(f"Do you wish to pick up where you left off, {self.player_name}? Enter 'Y' for yes or 'N' for no. ")
        if load == "Y":
            self.player.load_progress()
        elif load == "N":
            console.print("Loading canceled!\n")
        else:
            console.print("Invalid input!\n")

    def menu_choice_10(self):
        delete = console.input(f"Do you wish to start all over again, {self.player_name}? Enter 'Y' for yes or 'N' for no. ")
        if delete == "Y":
            self.player.delete_progress()
        elif delete == "N":
            console.print("Progress kept!\n")
        else:
            console.print("Invalid input!\n")
 
    def menu_choice_11(self):
        exit = console.input(f"Do you wish to exit :fire: SoulKeeper :fire:, {self.player_name}? Enter 'Y' for yes or 'N' for no. ")
        if exit == "Y":
            console.print(f"Farewell, {self.player_name}! Don't you dare go hollow :skull:!\n")
            self.access = False
        elif exit == "N":
            console.print("Returning to :fire: SoulKeeper :fire:...\n")
        else:
            console.print("Invalid input!\n")

    def choices(self):
        while self.access == True: 
            self.menu()

            self.choice = input("Choose an option: ")

            if self.choice == '1':
                self.menu_choice_1()
            elif self.choice == '2':
                self.menu_choice_2()
            elif self.choice == '3':
                self.menu_choice_3()
            elif self.choice == '4':
                self.menu_choice_4()
            elif self.choice == '5':
                self.menu_choice_5()
            elif self.choice == '6':
                self.menu_choice_6()
            elif self.choice == '7':
                self.menu_choice_7()
            elif self.choice == '8':
                self.menu_choice_8()
            elif self.choice == '9':
                self.menu_choice_9()
            elif self.choice == '10':
                self.menu_choice_10()
            elif self.choice == '11':
                self.menu_choice_11()
            else:
                console.print("Invaild option!\n")

    def run(self):
      self.start_app()
      self.access_menu()

if __name__== '__main__':
    main = Main()
    main.run()


