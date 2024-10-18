from player import Player

class Main:
    def __init__(self):
        self.player = Player("Marlon",total_souls=1000) # Start with 1000 souls
        
    def menu(self):
        print("\n--- SoulKeeper ---")

    def run(self):
        self.menu()

if __name__== '__main__':
    main = Main()
    main.run()


