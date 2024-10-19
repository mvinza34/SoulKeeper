import json # For saving and loading progress
import os # For deleting progress

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

    def show_status(self):
        # Show current souls and attribute levels
        print(f"\n{self.name}'s current status:")
        print(f"Souls: {self.total_souls}")
        for attribute, level in self.attributes.items():
            print(f"{attribute}: {level}")

    def get_total_level(self):
        # Show the overall level of the player
        return sum(self.attributes.values())

    def save_progress(self, filename="save.json"):
        data = {
            "attributes": self.attributes,
            "total_souls": self.total_souls
        }
        # Saves the player's progress into a JSON file
        with open(filename, 'w') as f:
            json.dump(data, f) 
        print("Progress saved!")

    def load_progress(self, filename="save.json"):
        # Reads the JSON file and loads the saved progress into the player's attributes and souls
        with open(filename, 'r') as f:
             data = json.load(f)
             self.attributes = data["attributes"]
             self.total_souls = data["total_souls"]
        print("Progress loaded!")

    def delete_progress(self):
        # Erases the json file so that the player can start new
        if os.path.exists("save.json"):
            os.remove("save.json")
            print("Progress deleted!")
        else:
            print("The file does not exist")




