from player import Player

class Main:
    def __init__(self):
        print("\n------ SoulKeeper ------\n")
        self.start = True
        self.access = False

    def start_app(self):
        # Prompt the user to enter a valid name and starting number of souls before proceeding
        while self.start:
            self.player_name = input("Welcome, Chosen Undead! Please enter your name: ").strip()

            if not self.player_name:
                print("You must enter a name.\n")
                continue

            try:
                self.player_souls = int(input("Enter how many souls you have: "))
                if self.player_souls < 0:
                    print("Souls must be a positive integer.\n")
                    continue
                self.start = False 
            except ValueError:
                print("You must enter a valid integer for souls.\n")

    def access_menu(self):
        # Grants user access to main menu 
        self.access = True
        self.player = Player(self.player_name, self.player_souls)
        print(f"Welcome, {self.player_name}, to SoulKeeper! You start with {self.player_souls} souls!\n")
        self.choices()

    def menu(self):
        print("1. Choose class")
        print("2. Level up attribute")
        print("3. View current stats")
        print("4. Add more souls")
        print("5. Show total souls spent")
        print("6. Save progress")
        print("7. Load progress")
        print("8. Delete progress")
        print("9. Exit\n")

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
                    print("You must first choose a class before leveling up!\n")
            elif self.choice == '3':
                if self.player.check_for_class == True:
                    self.player.show_status()
                else:
                    print("You must first choose a class before displaying your current status!\n")
            elif self.choice == '4':
                self.more_souls = int(input("Enter how many souls you wish to add: "))
                self.player.add_souls(self.more_souls)
            elif self.choice == '5':
                self.player.show_souls_spent()
            elif self.choice == '6':
                pass
                #self.player.save_progress()
            elif self.choice == '7':
                pass
                #self.player.load_progress()
            elif self.choice == '8':
                pass
                # erase = input("Do you wish to start all over again, Chosen Undead? Enter 'Y' for yes or any key for no. ")
                # if erase == "Y":
                #     self.player.delete_progress()
                # else:
                #     print("Progress kept!")
            elif self.choice == '9':
                print(f"Farewell, {self.player_name}! Don't you dare go hollow!\n")
                self.access = False
            else:
                print("Invaild option!\n")

    def run(self):
      self.start_app()
      self.access_menu()

if __name__== '__main__':
    main = Main()
    main.run()


