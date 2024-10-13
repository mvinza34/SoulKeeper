class Player:
    def __init__(self, name, starting_souls=1000):
        
        self.name = name
        self.souls = starting_souls

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

        self.base_cost = 100 # Base cost for leveling up any attribute




