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

    def level_up(self, attribute, base_cost=100, scaling_factor=1.2):
        # Calculate how many souls it costs to level up
        current_level = self.attributes[attribute]
        cost = int(base_cost * (current_level ** scaling_factor))

        # Spend souls to level up the desired attribute
        if self.total_souls >= cost:
            self.attributes[attribute] += 1
            self.total_souls -= cost
            print(f"{attribute} leveled up to {self.attributes[attribute]}!")
            print(f"Remaining souls: {self.total_souls}")
        else:
            print("Not enough souls!")



