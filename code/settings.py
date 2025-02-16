# Define the classes with starting levels, attributes, and perks
CLASSES = {
    "Warrior": {"Level": 4,
                "Vitality": 11, "Attunement": 8, "Endurance": 12, "Strength": 13,
                "Dexterity": 13, "Resistance": 11,  "Intelligence": 9, "Faith": 9,
                "Perks": {"Strength Cost Reduction": 0.6, "Dexterity Cost Reduction": 0.6}
                },

    "Knight": {"Level": 5, 
                "Vitality": 14, "Attunement": 10, "Endurance": 10, "Strength": 11,
                "Dexterity": 11, "Resistance": 10,  "Intelligence": 9, "Faith": 11,
                "Perks": {"Strength Cost Reduction": 0.4, "Dexterity Cost Reduction": 0.4}
                },

    "Wanderer": {"Level": 3, 
                    "Vitality": 10, "Attunement": 11, "Endurance": 10, "Strength": 10,
                    "Dexterity": 14, "Resistance": 12,  "Intelligence": 11, "Faith": 8,
                    "Perks": {"Strength Cost Reduction": 0.7, "Dexterity Cost Reduction": 0.5}
                },

    "Thief": {"Level": 5, 
                "Vitality": 9, "Attunement": 11, "Endurance": 9, "Strength": 9,
                "Dexterity": 15, "Resistance": 10,  "Intelligence": 12, "Faith": 11,
                "Perks": {"Strength Cost Reduction": 0.8, "Dexterity Cost Reduction": 0.4}
              },

    "Bandit": {"Level": 4, 
                "Vitality": 12, "Attunement": 8, "Endurance": 14, "Strength": 14,
                "Dexterity": 9, "Resistance": 11,  "Intelligence": 8, "Faith": 10,
                "Perks": {"Strength Cost Reduction": 0.4, "Dexterity Cost Reduction": 0.8}
                },

    "Hunter": {"Level": 4, 
                "Vitality": 11, "Attunement": 9, "Endurance": 11, "Strength": 12,
                "Dexterity": 14, "Resistance": 11,  "Intelligence": 9, "Faith": 9,
                "Perks": {"Strength Cost Reduction": 0.7, "Dexterity Cost Reduction": 0.7}
                },

    "Sorcerer": {"Level": 3, 
                    "Vitality": 8, "Attunement": 15, "Endurance": 8, "Strength": 9,
                    "Dexterity": 11, "Resistance": 8,  "Intelligence": 15, "Faith": 8,
                    "Perks": {"Intelligence Cost Reduction": 0.4, "Dexterity Cost Reduction": 0.6}
                },

    "Pyromancer": {"Level": 1, 
                    "Vitality": 10, "Attunement": 12, "Endurance": 11, "Strength": 12,
                    "Dexterity": 9, "Resistance": 12,  "Intelligence": 10, "Faith": 8,
                    "Perks": {"Intelligence Cost Reduction": 0.5, "Faith Cost Reduction": 0.5}
                  },

    "Cleric": {"Level": 2, 
                "Vitality": 11, "Attunement": 11, "Endurance": 9, "Strength": 12,
                "Dexterity": 8, "Resistance": 11,  "Intelligence": 8, "Faith": 14,
                "Perks": {"Faith Cost Reduction": 0.4, "Strength Cost Reduction": 0.6}
               },

    "Deprived": {"Level": 6, 
                    "Vitality": 11, "Attunement": 11, "Endurance": 11, "Strength": 11,
                    "Dexterity": 11, "Resistance": 11,  "Intelligence": 11, "Faith": 11,
                    "Perks": {"Strength Cost Reduction": 0.8, "Dexterity Cost Reduction": 0.8}
                }
}

 # Define the achievements that the user must unlock
ACHIEVEMENTS = {"Create a Class": False, "Reach Level 10": False, "Spend 1,000 Souls": False, "Spend 10,000 Souls": False}

SOULS_SPENT_PER_ATTRIBUTE = {  # Track souls spent per attribute
            "Vitality": 0, "Attunement": 0, "Endurance": 0, "Strength": 0, 
            "Dexterity": 0, "Resistance": 0, "Intelligence": 0, "Faith": 0
        }
