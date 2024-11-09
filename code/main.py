from player import Player

class Main:
    def __init__(self):
        self.player = Player("Marlon",total_souls=3000) # Start with 3000 souls
        
    def menu(self):
        print("1. Choose class")
        print("2. Level up attribute")
        print("3. View current stats")
        print("4. Save progress")
        print("5. Load progress")
        print("6. Delete progress")
        print("7. Exit")

    def run(self):
        print("\n--- SoulKeeper ---")
        print("Welcome, Chosen Undead!")

        while True: 
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
                pass
                #self.player.save_progress()
            elif self.choice == '5':
                pass
                #self.player.load_progress()
            elif self.choice == '6':
                pass
                # erase = input("Do you wish to start all over again, Chosen Undead? Enter 'Y' for yes or any key for no. ")
                # if erase == "Y":
                #     self.player.delete_progress()
                # else:
                #     print("Progress kept!")
            elif self.choice == '7':
                print("Farewell, Chosen Undead! Don't you dare go hollow!")
                break
            else:
                print("Invaild option!")

if __name__== '__main__':
    main = Main()
    main.run()


