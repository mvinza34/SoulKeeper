import json # For saving and loading progress
import os # For deleting progress
import random 

import settings

from rich.console import Console # For console output (i.e., colors, emojis, etc.)
from rich.table import Table # For creating tables in the console

from quest import Quest 

console = Console()

class Player:
    def __init__(self, name, total_souls):
        
        self.name = name # Name of the player
        self.total_souls = total_souls # Starting amount of souls
        self.total_souls_spent = 0 # Tracks total amount of souls spent

        self.classes = settings.CLASSES 
        self.achievements = settings.ACHIEVEMENTS
        self.souls_spent_per_attribute = settings.SOULS_SPENT_PER_ATTRIBUTE

        self.check_for_class = False # Check if the user chose a starting class
        self.quests = []  # List to store quests

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
        cost = int(base_cost * ((current_level) ** scaling_factor) * cost_multiplier)

        # Spend souls to level up the desired attribute
        if self.total_souls >= cost:
            selected_class[attribute] += 1
            selected_class["Level"] += 1  # Increment the level by 1
            self.total_souls -= cost
            self.total_souls_spent += cost # Keep track of total amount of spent souls
            self.souls_spent_per_attribute[attribute] += cost # Update the souls spent on the attribute
            self.check_achievements()
            self.check_quests()

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
            self.check_achievements()
        else:
            print("Invalid class!\n")

    def level_up(self):
        self.attribute = input("Enter an attribute to level up (Vitality, Attunement, Endurance, Strength, Dexterity, Resistance, Intelligence, Faith): ")
        if self.attribute in self.selected_class:
            self.increase_attribute_level(self.selected_class, self.attribute)
            self.random_event()
        else:
            print("Invaild attribute!\n")

    def show_status(self):
        # Create a table displaying the class, current level, current atrributes, and current souls
        status_table = Table(title=f"{self.name}'s Current Status:")
        status_table.add_column("Stat", style="cyan")
        status_table.add_column("Value", justify='right')
        status_table.add_row("Class", self.starting_class_name)
        
        for stat, value in self.selected_class.items():
            if stat != "Perks":
                status_table.add_row(stat, str(value))

        status_table.add_row("Souls", str(self.total_souls))
         
        console.print(status_table)

        # Create a table displaying all the perks depending on the class
        if "Perks" in self.selected_class:
            perks_table = Table(title="Perks", show_header=True, header_style="bold magenta")
            perks_table.add_column("Perk", style="green")
            perks_table.add_column("Value", justify="right")
    
        for perk, value in self.selected_class["Perks"].items():
            perks_table.add_row(perk, str(value))

        console.print(perks_table)

    def show_souls_spent(self):
        self.show_souls_spent_per_attribute()
        console.print(f"Total Amount of Souls Spent: {self.total_souls_spent} :fire:\n")

    def show_souls_spent_per_attribute(self):
        # Create a table displaying the amount of souls spent for each attribute
        souls_spent_per_attribute_table = Table(title="Souls Spent Per Attribute", show_header=True, header_style="bold magenta")
        souls_spent_per_attribute_table.add_column("Attribute", style="cyan")
        souls_spent_per_attribute_table.add_column("Souls Spent", style="green", justify="right")

        for attribute, souls_spent in self.souls_spent_per_attribute.items():
            souls_spent_per_attribute_table.add_row(attribute, str(souls_spent))

        console.print(souls_spent_per_attribute_table)
 
    def unlock_achievement(self, name):
        if name in self.achievements and not self.achievements[name]:
           self.achievements[name] = True
           console.print(f":tada: Achievement Unlocked: {name}!\n")

    def check_achievements(self):
        # General Achievements
        if self.check_for_class == True:
            self.unlock_achievement("Create a Class")

        # Leveling Achievements
        if self.selected_class["Level"] >= 10:
            self.unlock_achievement("Reach Level 10")
        if self.selected_class["Level"] >= 50:
            self.unlock_achievement("Reach Level 50")
        if self.selected_class["Level"] >= 100:
            self.unlock_achievement("Reach Level 100")
        if self.selected_class["Level"] >= 150:
            self.unlock_achievement("Reach Level 150")
        if self.selected_class["Level"] >= 200:
            self.unlock_achievement("Reach Level 200")
        if self.selected_class["Level"] >= 250:
            self.unlock_achievement("Reach Level 250")
        if self.selected_class["Level"] >= 300:
            self.unlock_achievement("Reach Level 300")

        # Soul Hoarding Achievements
        if self.total_souls >= 10000:
            self.unlock_achievement("Soul Hoarder")
        if self.total_souls >= 1000000:
            self.unlock_achievement("Soul Millionaire")
        if self.total_souls >= 1000000000:
            self.unlock_achievement("Soul Keeper")

        # Soul Spending Achievements
        if self.total_souls_spent >= 1000:
            self.unlock_achievement("Small Spender")
        if self.total_souls_spent >= 10000:
            self.unlock_achievement("Medium Spender")
        if self.total_souls_spent >= 50000:
            self.unlock_achievement("Big Spender")
        if self.total_souls_spent >= 500000:
            self.unlock_achievement("Ultimate Spender")

        # Attribute Leveling Achievements
        if self.selected_class["Vitality"] >= 50:
            self.unlock_achievement("Vitality Master")
        if self.selected_class["Attunement"] >= 50:
            self.unlock_achievement("Attunement Prodigy")
        if self.selected_class["Endurance"] >= 40:
            self.unlock_achievement("Endurance Dynamo")
        if self.selected_class["Strength"] >= 40:
            self.unlock_achievement("Strength Champion")
        if self.selected_class["Dexterity"] >= 45:
            self.unlock_achievement("Dexterity Expert")
        if self.selected_class["Resistance"] >= 30:
            self.unlock_achievement("Resistance Tank")
        if self.selected_class["Intelligence"] >= 50:
            self.unlock_achievement("Intelligence Sage")
        if self.selected_class["Faith"] >= 50:
            self.unlock_achievement("Faith Prophet")

        # Character Build Achievements
        if self.selected_class["Level"] >= 150 and self.starting_class_name == "Warrior":
            self.unlock_achievement("Warrior's Path")
        if self.selected_class["Level"] >= 150 and self.starting_class_name == "Knight":
            self.unlock_achievement("Knight's Honor")
        if self.selected_class["Level"] >= 150 and self.starting_class_name == "Wanderer":
            self.unlock_achievement("Wanderer's Resilience")
        if self.selected_class["Level"] >= 150 and self.starting_class_name == "Thief":
            self.unlock_achievement("Thief's Cunning")
        if self.selected_class["Level"] >= 150 and self.starting_class_name == "Bandit":
            self.unlock_achievement("Bandit's Savagery")
        if self.selected_class["Level"] >= 150 and self.starting_class_name == "Hunter":
            self.unlock_achievement("Hunter's Precision")
        if self.selected_class["Level"] >= 150 and self.starting_class_name == "Sorcerer":
            self.unlock_achievement("Sorcerer's Wisdom")
        if self.selected_class["Level"] >= 150 and self.starting_class_name == "Pyromancer":
            self.unlock_achievement("Pyromancer's Flame")
        if self.selected_class["Level"] >= 150 and self.starting_class_name == "Cleric":
            self.unlock_achievement("Cleric's Devotion")
        if self.selected_class["Level"] >= 150 and self.starting_class_name == "Deprived":
            self.unlock_achievement("Deprived's Struggle")

    def view_achievements(self):
        # Group the achievements by category
        categories = {
            "General Milestones": {
                "Create a Class"
            },

            "Leveling Milestones": {
                "Reach Level 10", "Reach Level 50", "Reach Level 100", "Reach Level 150", 
                "Reach Level 200", "Reach Level 250", "Reach Level 300"
            },

            "Soul Spending": {
                "Small Spender", "Medium Spender", "Big Spender", "Ultimate Spender"
            },

            "Attribute Mastery": {
                "Vitality Master", "Attunement Prodigy", "Endurance Dynamo", "Strength Champion", 
                "Dexterity Expert", "Resistance Tank", "Intelligence Sage", "Faith Prophet"
            },

            "Character Builds": {
                 "Warrior's Path", "Knight's Honor", "Wanderer's Resilience",  "Thief's Cunning",
                 "Bandit's Savagery", "Hunter's Precision", "Sorcerer's Wisdom", "Pyromancer's Flame",
                 "Cleric's Devotion",  "Deprived's Struggle"
            }
        }

        # Create a table displaying all achievements, locked or unlocked
        achievements_table = Table(title=":trophy: Achievements :trophy:", show_header=True, header_style="bold magenta")
        achievements_table.add_column("Category", style="gold1", justify="left")
        achievements_table.add_column("Achievement", style="cyan", justify="left")
        achievements_table.add_column("Status", style="green", justify="center")

        for category, achievements in categories.items():
            for achievement in achievements:
                status = ":heavy_check_mark: Unlocked" if self.achievements.get(achievement, False) else ":x: Locked"
                achievements_table.add_row(category, achievement, status)
                category = "" # Ensures that the category is only displayed once
        
        console.print(achievements_table)

    def random_event(self):
        event_chance = random.random()

        # Soul gains or losses based on random events
        if event_chance < 0.5: # 10% chance of a random event
            bonus = random.randint(100,1000)
            self.total_souls += bonus
            console.print(f":sparkles: You found {bonus} extra souls :fire:! You now have a total of {self.total_souls} souls! Good for you! :sparkles:\n")
        elif event_chance < 0.3: # Another 10% chance 
            penalty = random.randint(50, 1000)
            self.total_souls -= penalty
            console.print(f":ghost: An enemy broke into SoulKeeper and stole {penalty} souls from you! You now have {self.total_souls} souls left! Too bad! :ghost:\n")
        elif event_chance < 0.15:
            jackpot = random.randint(10000, 50000)
            self.total_souls += jackpot
            console.print(f":star2: Face it, Tiger...You've just hit the jackpot and found a hidden cache with {jackpot} souls! You now have a total of {self.total_souls} souls! Lucky you! :star2:\n")
        
        # Attribute gains based on random events
        elif event_chance < 0.49:
            self.selected_class["Vitality"] += 3
            console.print(":green_heart: You feel invigorated! Vitality increased by 3 (free of charge)!")
        elif event_chance < 0.45:
            self.selected_class["Attunement"] += 1
            console.print(":green_heart: You feel like you mastered a new spell! Attunement increased by 1 (free of charge)!")
        elif event_chance < 0.49:
            self.selected_class["Endurance"] += 1
            console.print(":green_heart: You feel energized! Endurance increased by 1 (free of charge)!")
        elif event_chance < 0.47:
            self.selected_class["Strength"] += 2
            console.print(":green_heart: You feel like you've gotten stronger! Strength increased by 2 (free of charge)!")
        elif event_chance < 0.45:
            self.selected_class["Dexterity"] += 2
            console.print(":green_heart: You feel like your hands can do anything! Dexterity increased by 2 (free of charge)!")
        elif event_chance < 0.41:
            self.selected_class["Resistance"] += 1
            console.print(":green_heart: You feel like you've become durable! Resistance increased by 1 (free of charge)!")
        elif event_chance < 0.48:
            self.selected_class["Intelligence"] += 2
            console.print(":green_heart: You feel like you are strong with magic! Intelligence increased by 2 (free of charge)!")
        elif event_chance < 0.48:
            self.selected_class["Faith"] += 2
            console.print(":green_heart: You feel like you are blessed by the gods! Faith increased by 2 (free of charge)!")

        # Attribute losses based on random events
        elif event_chance < 0.29:
            self.selected_class["Vitality"] = max(0, self.selected_class["Vitality"] - 3)
            console.print(":broken_heart: You feel your life force depleting. Vitality decreased by 3.")
        elif event_chance < 0.25:
            self.selected_class["Attunement"] = max(0, self.selected_class["Attunement"] - 1)
            console.print(":broken_heart: You feel your knowledge in spells getting rusty. Attunement decreased by 1.")
        elif event_chance < 0.29:
            self.selected_class["Endurance"] = max(0, self.selected_class["Endurance"] - 1)
            console.print(":broken_heart: You feel your energy getting weaker. Endurance decreased by 1.")
        elif event_chance < 0.27:
            self.selected_class["Strength"] = max(0, self.selected_class["Strength"] - 2)
            console.print(":broken_heart: You feel weakened. Strength decreased by 2.")
        elif event_chance < 0.25:
            self.selected_class["Dexterity"] = max(0, self.selected_class["Dexterity"] - 2)
            console.print(":broken_heart: You feel like your hands are failing you. Dexterity decreased by 2.")
        elif event_chance < 0.21:
            self.selected_class["Resistance"] = max(0, self.selected_class["Resistance"] - 1)
            console.print(":broken_heart: You feel your body crumbling from within. Resistance decreased by 1.")
        elif event_chance < 0.28:
            self.selected_class["Intelligence"] = max(0, self.selected_class["Intelligence"] - 2)
            console.print(":broken_heart: You feel your magic reserves decreasing. Intelligence decreased by 2.")
        elif event_chance < 0.28:
            self.selected_class["Faith"] = max(0, self.selected_class["Faith"] - 2)
            console.print(":broken_heart: You feel like the gods have forsaken you. Faith decreased by 2.")

    def add_quest(self, quest):
        self.quests.append(quest)
        console.print(f"New Quest Added: {quest.name}\n")

    def check_quests(self):
        for quest in self.quests:
            if not quest.completed:
                quest.check_completion(self)

    def show_quests(self):
        quest_table = Table(title="Quests", show_header=True, header_style="bold magenta")
        quest_table.add_column("Name", style="cyan")
        quest_table.add_column("Description", style="green")
        quest_table.add_column("Status", style="yellow")

        for quest in self.quests:
            status = "Completed" if quest.completed else "Incomplete"
            quest_table.add_row(quest.name, quest.description, status)

        console.print(quest_table)
            
    def save_progress(self, filename="save.json"):
        data = {
            "name": self.name,
            "quests": [q.quests_to_dict() for q in self.quests], # JSON serializable representation of quests
            "achievements": self.achievements,
            "total_souls": self.total_souls,
            "total_souls_spent": self.total_souls_spent,
            "souls_spent_per_attribute": self.souls_spent_per_attribute,
            "selected_class": self.starting_class_name,
            "attributes": self.selected_class
        }
        # Saves the player's progress into a JSON file
        with open(filename, 'w') as f:
            json.dump(data, f) 
        console.print("Progress saved!\n")

    def load_progress(self, filename="save.json"):
        if os.path.exists("save.json"):
            # Reads the JSON file and loads the saved progress so that the player can pick up where they left off
            with open(filename, 'r') as f:
                 data = json.load(f)
                 self.name = data["name"]
                 self.quests = [Quest.quests_from_dict(q) for q in data.get("quests", [])] # No comma so self.show_quests() works properly
                 self.achievements = data.get("achievements", self.achievements)
                 self.total_souls = data["total_souls"]
                 self.total_souls_spent = data["total_souls_spent"]
                 self.souls_spent_per_attribute = data.get("souls_spent_per_attribute", self.souls_spent_per_attribute)
                 self.starting_class_name = data["selected_class"]
                 self.selected_class = data["attributes"]
                 self.check_for_class = True
            console.print("Progress loaded!\n")
        else:
            console.print("The file does not exist!\n")

    def delete_progress(self):
        # Erases the json file so that the player can start new
        if os.path.exists("save.json"):
            os.remove("save.json")
            console.print("Progress deleted!\n")
        else:
            console.print("The file does not exist!\n")




