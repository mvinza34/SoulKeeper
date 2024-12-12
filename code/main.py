from player import Player

class Main:
    def __init__(self):
        print("\n--- SoulKeeper ---")
        self.start = True
        self.access = False

    def start_app(self):
        # Prompt the user to enter a valid name and starting number of souls before proceeding
        while self.start:
            self.player_name = input("Welcome, Chosen Undead! Please enter your name: ").strip()

            if not self.player_name:
                print("You must enter a name.")
                continue

            try:
                self.player_souls = int(input("Enter how many souls you have: "))
                if self.player_souls < 0:
                    print("Souls must be a positive integer.")
                    continue
                self.start = False 
            except ValueError:
                print("You must enter a valid integer for souls.")

    def access_menu(self):
        # Grants user access to main menu 
        self.access = True
        self.player = Player(self.player_name, self.player_souls)
        print(f"Welcome, {self.player_name}, to SoulKeeper! You start with {self.player_souls} souls!")
        self.choices()

    def menu(self):
        print("1. Choose class")
        print("2. Level up attribute")
        print("3. View current stats")
        print("4. Add more souls")
        print("5. Save progress")
        print("6. Load progress")
        print("7. Delete progress")
        print("8. Exit")

    def choices(self):
        while self.access == True: 
            self.menu()

            self.choice = input("Choose an option: ")

            if self.choice == '1':
                self.player.choose_class()
            elif self.choice == '2':
                if self.player.check_for_class == True:
                    self.player.level_up()
                else:
                    print("You must first choose a class before leveling up!")
            elif self.choice == '3':
                if self.player.check_for_class == True:
                    self.player.show_status()
                else:
                    print("You must first choose a class before displaying your current status!")
            elif self.choice == '4':
                self.more_souls = int(input("Enter how many souls you wish to add: "))
                self.player.add_souls(self.more_souls)
            elif self.choice == '5':
                pass
                #self.player.save_progress()
            elif self.choice == '6':
                pass
                #self.player.load_progress()
            elif self.choice == '7':
                pass
                # erase = input("Do you wish to start all over again, Chosen Undead? Enter 'Y' for yes or any key for no. ")
                # if erase == "Y":
                #     self.player.delete_progress()
                # else:
                #     print("Progress kept!")
            elif self.choice == '8':
                print(f"Farewell, {self.player_name}! Don't you dare go hollow!")
                self.access = False
            else:
                print("Invaild option!")

    def run(self):
      self.start_app()
      self.access_menu()

if __name__== '__main__':
    main = Main()
    main.run()


