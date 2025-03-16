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
        # Check if the player meets the requirements to complete the quest
        for requirement, value in self.requirements.items():
            if isinstance(requirement, tuple):
                # Handle nested attributes or dictionary keys
                attr, key = requirement
                if getattr(player, attr)[key] < value:
                    return False
            else:
                if getattr(player, requirement) < value:
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
