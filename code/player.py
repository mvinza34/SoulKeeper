class Player:
    def __init__(self, name, total_souls):
        
        self.name = name # Name of the player
        self.total_souls = total_souls # Starting amount of souls

        # Define the attributes with initial levels
        self.attributes = {
            "Vitality": 1,
            "Attunment": 1,
            "Endurance": 1,
            "Strength": 1,
            "Dexterity": 1,
            "Resistance": 1, 
            "Intelligence": 1,
            "Faith": 1
            }

    def level_up(self):
        self.base_cost = 100 # Base cost for leveling up any attribute






