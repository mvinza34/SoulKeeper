from player import Player

class Main:
    def __init__(self):
        self.player = Player("Marlon",total_souls=3000) # Start with 3000 souls
        
    def menu(self):
        print("\n--- SoulKeeper ---")
        print("1. Level up attribute")
        print("2. View current stats")
        print("3. Save progress")
        print("4. Load progress")
        print("5. Delete progress")
        print("6. Exit")

    def run(self):
        while True: 
            self.menu()

            self.choice = input("Choose an option: ")

            if self.choice == '1':
                self.player.level_up()
            elif self.choice == '2':
                self.player.show_status()
            elif self.choice == '3':
                pass
                #self.player.save_progress()
            elif self.choice == '4':
                pass
                #self.player.load_progress()
            elif self.choice == '5':
                pass
                # erase = input("Do you wish to start all over again, Chosen Undead? Enter 'Y' for yes or any key for no. ")
                # if erase == "Y":
                #     self.player.delete_progress()
                # else:
                #     print("Progress kept!")
            elif self.choice == '6':
                print("Farewell, Chosen Undead! Don't you dare go hollow!")
                break
            else:
                print("Invaild option!")

if __name__== '__main__':
    main = Main()
    main.run()


