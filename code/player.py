import json # For saving and loading progress
import os # For deleting progress

class Player:
    def __init__(self, name, total_souls):
        
        self.name = name # Name of the player
        self.total_souls = total_souls # Starting amount of souls
        self.total_souls_spent = 0 # Tracks total amount of souls spent

        # Define the classes with starting level and attributes
        self.classes = {
            "Warrior": {"Level": 4, "Vitality": 11, "Attunement": 8, "Endurance": 12, "Strength": 13, "Dexterity": 13, "Resistance": 11,  "Intelligence": 9, "Faith": 9},
            "Knight": {"Level": 5, "Vitality": 14, "Attunement": 10, "Endurance": 10, "Strength": 11, "Dexterity": 11, "Resistance": 10,  "Intelligence": 9, "Faith": 11},
            "Wanderer": {"Level": 3, "Vitality": 10, "Attunement": 11, "Endurance": 10, "Strength": 10, "Dexterity": 14, "Resistance": 12,  "Intelligence": 11, "Faith": 8},
            "Thief": {"Level": 5, "Vitality": 9, "Attunement": 11, "Endurance": 9, "Strength": 9, "Dexterity": 15, "Resistance": 10,  "Intelligence": 12, "Faith": 11},
            "Bandit": {"Level": 4, "Vitality": 12, "Attunement": 8, "Endurance": 14, "Strength": 14, "Dexterity": 9, "Resistance": 11,  "Intelligence": 8, "Faith": 10},
            "Hunter": {"Level": 4, "Vitality": 11, "Attunement": 9, "Endurance": 11, "Strength": 12, "Dexterity": 14, "Resistance": 11,  "Intelligence": 9, "Faith": 9},
            "Sorcerer": {"Level": 3, "Vitality": 8, "Attunement": 15, "Endurance": 8, "Strength": 9, "Dexterity": 11, "Resistance": 8,  "Intelligence": 15, "Faith": 8},
            "Pyromancer": {"Level": 1, "Vitality": 10, "Attunement": 12, "Endurance": 11, "Strength": 12, "Dexterity": 9, "Resistance": 12,  "Intelligence": 10, "Faith": 8},
            "Cleric": {"Level": 2, "Vitality": 11, "Attunement": 11, "Endurance": 9, "Strength": 12, "Dexterity": 8, "Resistance": 11,  "Intelligence": 8, "Faith": 14},
            "Deprived": {"Level": 6, "Vitality": 11, "Attunement": 11, "Endurance": 11, "Strength": 11, "Dexterity": 11, "Resistance": 11,  "Intelligence": 11, "Faith": 11}
        }

        # Checks if the user chose a starting class
        self.check_for_class = False

    def add_souls(self, souls_to_add):
        try:
            if souls_to_add < 0:
                print("Souls must be a positive integer.")
            else:
                print(f"Current souls: {self.total_souls}, Added souls: {souls_to_add}")
                self.total_souls += souls_to_add
                print(f"Souls updated! Total souls: {self.total_souls}")
        except ValueError:
            print("You must enter a valid integer for souls.")

    def increase_attribute_level(self, selected_class, attribute, base_cost=50, scaling_factor=1.2):
        # Get the current level of the attribute in the chosen class
        current_level = selected_class[attribute]

        # Calculate how many souls it costs to level up
        cost = int(base_cost * (current_level ** scaling_factor))

        # Spend souls to level up the desired attribute
        if self.total_souls >= cost:
            selected_class[attribute] += 1
            selected_class["Level"] += 1  # Increment the level by 1
            self.total_souls -= cost
            self.total_souls_spent += cost # Keep track of spent souls
            print(f"You spent {cost} souls to level up.")
            print(f"{attribute} leveled up to {selected_class[attribute]}!")
            print(f"Your soul level is now {selected_class['Level']}!")
            print(f"Remaining souls: {self.total_souls}")
        else:
            print("Not enough souls!")

    def choose_class(self):
        self.starting_class_name = input("Choose a starting class: ").strip()
        if self.starting_class_name in self.classes:
            print(f"You chose to start as a {self.starting_class_name}.")
            self.selected_class = self.classes[self.starting_class_name]
            print(f"Your current soul level is {self.selected_class['Level']}.")
            self.check_for_class = True
        else:
            print("Invalid class!")

    def level_up(self):
        self.attribute = input("Enter an attribute to level up (Vitality, Attunement, Endurance, Strength, Dexterity, Resistance, Intelligence, Faith): ")
        if self.attribute in self.selected_class:
            self.increase_attribute_level(self.selected_class, self.attribute)
        else:
            print("Invaild attribute!")

    def show_status(self):
        # Display the class, current level, current atrributes, and current souls
        print(f"\n{self.name}'s current status:")
        print(f"Class: {self.starting_class_name}")
        for stat, value in self.selected_class.items():
            print(f"{stat}: {value}")
        print(f"Souls: {self.total_souls}")

    def show_souls_spent(self):
        print(f"Total Souls Spent: {self.total_souls_spent}\n")

    # def save_progress(self, filename="save.json"):
    #     data = {
    #         "attributes": self.attributes,
    #         "total_souls": self.total_souls
    #     }
    #     # Saves the player's progress into a JSON file
    #     with open(filename, 'w') as f:
    #         json.dump(data, f) 
    #     print("Progress saved!")

    # def load_progress(self, filename="save.json"):
    #     # Reads the JSON file and loads the saved progress into the player's attributes and souls
    #     with open(filename, 'r') as f:
    #          data = json.load(f)
    #          self.attributes = data["attributes"]
    #          self.total_souls = data["total_souls"]
    #     print("Progress loaded!")

    # def delete_progress(self):
    #     # Erases the json file so that the player can start new
    #     if os.path.exists("save.json"):
    #         os.remove("save.json")
    #         print("Progress deleted!")
    #     else:
    #         print("The file does not exist")




