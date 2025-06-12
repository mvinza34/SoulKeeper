from rich.console import Console # For console output (i.e., colors, emojis, etc.)

console = Console()

class Quest:
    def __init__(self, name, description, requirements, rewards):
        self.name = name
        self.description = description
        self.requirements = requirements
        self.rewards = rewards
        self.completed = False

    def check_completion(self, player):
        for requirement, value in self.requirements.items():
            if isinstance(requirement, tuple):
                # Nested attribute or dict key, e.g., ("selected_class", "Level")
                attr, key = requirement
                attr_value = getattr(player, attr)

                if isinstance(attr_value, dict):
                    if attr_value[key] < value:
                        return False
                else:
                    # If not a dict, treat as object attribute
                    if getattr(attr_value, key) < value:
                        return False
            else:
                # Direct attribute, e.g., "selected_class"
                attr_value = getattr(player, requirement)

                if isinstance(attr_value, dict):
                    # If requirement is a dict, value should be a key to check
                    # (not used in current quests, but safe to handle)
                    if value not in attr_value:
                        return False
                elif isinstance(attr_value, str):
                    # Compare string equality (e.g., class name)
                    if attr_value != value:
                        return False
                else:
                    # Fallback for numeric comparison
                    if attr_value < value:
                        return False

        self.completed = True
        self.give_rewards(player)
        return True

    def give_rewards(self, player):
        # Give rewards to the player
        for reward, value in self.rewards.items():
            if isinstance(reward, tuple):
                attr, key = reward
                getattr(player, attr)[key] += value
            else:
                setattr(player, reward, getattr(player, reward) + value)
        console.print(f"Quest Completed: {self.name}! Rewards: {self.rewards}\n")
