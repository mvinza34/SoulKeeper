import json # For saving and loading progress
import os # For deleting progress

from rich.console import Console
from rich.table import Table

console = Console()

class Player:
    def __init__(self, name, total_souls):
        
        self.name = name # Name of the player
        self.total_souls = total_souls # Starting amount of souls
        self.total_souls_spent = 0 # Tracks total amount of souls spent

        # Define the classes with starting level and attributes
        self.classes = {
            "Warrior": {"Level": 4,
                       "Vitality": 11, "Attunement": 8, "Endurance": 12, "Strength": 13, "Dexterity": 13, "Resistance": 11,  "Intelligence": 9, "Faith": 9,
                        "Perks": {"Strength Cost Reduction": 0.6, "Dexterity Cost Reduction": 0.6}
                        },
            "Knight": {"Level": 5, 
                       "Vitality": 14, "Attunement": 10, "Endurance": 10, "Strength": 11, "Dexterity": 11, "Resistance": 10,  "Intelligence": 9, "Faith": 11,
                       "Perks": {"Strength Cost Reduction": 0.4, "Dexterity Cost Reduction": 0.4}
                       },
            "Wanderer": {"Level": 3, 
                         "Vitality": 10, "Attunement": 11, "Endurance": 10, "Strength": 10, "Dexterity": 14, "Resistance": 12,  "Intelligence": 11, "Faith": 8,
                         "Perks": {"Strength Cost Reduction": 0.7, "Dexterity Cost Reduction": 0.5}
                         },
            "Thief": {"Level": 5, 
                      "Vitality": 9, "Attunement": 11, "Endurance": 9, "Strength": 9, "Dexterity": 15, "Resistance": 10,  "Intelligence": 12, "Faith": 11,
                      "Perks": {"Strength Cost Reduction": 0.8, "Dexterity Cost Reduction": 0.4}
                      },
            "Bandit": {"Level": 4, 
                       "Vitality": 12, "Attunement": 8, "Endurance": 14, "Strength": 14, "Dexterity": 9, "Resistance": 11,  "Intelligence": 8, "Faith": 10,
                       "Perks": {"Strength Cost Reduction": 0.4, "Dexterity Cost Reduction": 0.8}
                       },
            "Hunter": {"Level": 4, 
                       "Vitality": 11, "Attunement": 9, "Endurance": 11, "Strength": 12, "Dexterity": 14, "Resistance": 11,  "Intelligence": 9, "Faith": 9,
                       "Perks": {"Strength Cost Reduction": 0.7, "Dexterity Cost Reduction": 0.7}
                       },
            "Sorcerer": {"Level": 3, 
                         "Vitality": 8, "Attunement": 15, "Endurance": 8, "Strength": 9, "Dexterity": 11, "Resistance": 8,  "Intelligence": 15, "Faith": 8,
                         "Perks": {"Intelligence Cost Reduction": 0.4, "Dexterity Cost Reduction": 0.6}
                         },
            "Pyromancer": {"Level": 1, 
                           "Vitality": 10, "Attunement": 12, "Endurance": 11, "Strength": 12, "Dexterity": 9, "Resistance": 12,  "Intelligence": 10, "Faith": 8,
                           "Perks": {"Intelligence Cost Reduction": 0.5, "Faith Cost Reduction": 0.5}
                           },
            "Cleric": {"Level": 2, 
                       "Vitality": 11, "Attunement": 11, "Endurance": 9, "Strength": 12, "Dexterity": 8, "Resistance": 11,  "Intelligence": 8, "Faith": 14,
                       "Perks": {"Faith Cost Reduction": 0.4, "Strength Cost Reduction": 0.6}
                       },
            "Deprived": {"Level": 6, 
                         "Vitality": 11, "Attunement": 11, "Endurance": 11, "Strength": 11, "Dexterity": 11, "Resistance": 11,  "Intelligence": 11, "Faith": 11,
                         "Perks": {"Strength Cost Reduction": 0.8, "Dexterity Cost Reduction": 0.8}
                         }
        }

        # Checks if the user chose a starting class
        self.check_for_class = False

    def add_souls(self, souls_to_add):
        try:
            if souls_to_add < 0:
                print("Souls must be a positive integer.\n")
            else:
                console.print(f"Current souls: {self.total_souls} :fire:, Added souls: {souls_to_add} :fire:")
                self.total_souls += souls_to_add
                console.print(f"Souls updated! Total souls: {self.total_souls} :fire:\n")
        except ValueError:
            print("You must enter a valid integer for souls.\n")

    def increase_attribute_level(self, selected_class, attribute, base_cost=50, scaling_factor=1.2):
        # Get the current level of the attribute in the chosen class
        current_level = selected_class[attribute]

        cost_multiplier = self.selected_class.get("Perks", {}).get(f"{attribute} Cost Reduction", 1.0)

        # Calculate how many souls it costs to level up
        cost = int(base_cost * (current_level ** scaling_factor) * cost_multiplier)

        # Spend souls to level up the desired attribute
        if self.total_souls >= cost:
            selected_class[attribute] += 1
            selected_class["Level"] += 1  # Increment the level by 1
            self.total_souls -= cost
            self.total_souls_spent += cost # Keep track of spent souls
            console.print(f"You spent {cost} souls to level up.")
            console.print(f"{attribute} leveled up to {selected_class[attribute]}!")
            console.print(f"Your soul level is now {selected_class['Level']}!")
            console.print(f"Remaining souls: {self.total_souls}\n")
        else:
            print("Not enough souls!\n")

    def choose_class(self):
        self.starting_class_name = input("Choose a starting class: ").strip()
        if self.starting_class_name in self.classes:
            print(f"You chose to start as a {self.starting_class_name}.")
            self.selected_class = self.classes[self.starting_class_name]
            console.print(f"Your current soul level is {self.selected_class['Level']}.\n")
            self.check_for_class = True
        else:
            print("Invalid class!\n")

    def level_up(self):
        self.attribute = input("Enter an attribute to level up (Vitality, Attunement, Endurance, Strength, Dexterity, Resistance, Intelligence, Faith): ")
        if self.attribute in self.selected_class:
            self.increase_attribute_level(self.selected_class, self.attribute)
        else:
            print("Invaild attribute!\n")

    def show_status(self):
        # Display the class, current level, current atrributes, and current souls
        status_table = Table(title=f"{self.name}'s Current Status:")
        status_table.add_column("Stat", style="cyan")
        status_table.add_column("Value", justify='right')
        status_table.add_row("Class", self.starting_class_name)
        
        for stat, value in self.selected_class.items():
            if stat != "Perks":
                status_table.add_row(stat, str(value))

        status_table.add_row("Souls", str(self.total_souls))
         
        console.print(status_table)

        # Display the perks depending on the class
        if "Perks" in self.selected_class:
            perks_table = Table(title="Perks", show_header=True, header_style="bold magenta")
            perks_table.add_column("Perk", style="green")
            perks_table.add_column("Value", justify="right")
    
        for perk, value in self.selected_class["Perks"].items():
            perks_table.add_row(perk, str(value))

        console.print(perks_table)

    def show_souls_spent(self):
        console.print(f"Total Souls Spent: {self.total_souls_spent} :fire:\n")

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




