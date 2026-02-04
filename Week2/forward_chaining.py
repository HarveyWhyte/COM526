class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion

class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = set()

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_fact(self, fact):
        self.facts.add(fact)

    def ask_user_for_fact(self, fact):
        response = input(f"Is it true that {fact}? (yes/no): ").strip().lower()
        if response == 'yes':
            self.add_fact(fact)

    def infer(self):
        new_facts = True
        while new_facts:
            new_facts = False
            for rule in self.rules:
                if all(condition in self.facts for condition in rule.conditions) and rule.conclusion not in self.facts:
                    self.facts.add(rule.conclusion)
                    new_facts = True
                    print(f"Inferred: {rule.conclusion}")
                elif any(condition not in self.facts for condition in rule.conditions):
                    for condition in rule.conditions:
                        if condition not in self.facts:
                            self.ask_user_for_fact(condition)
                            break # Ask one fact at a time




class Item:
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes

class ExpertSystem2:
    def __init__(self):
        self.items = []
        self.inferredAttributes: dict[str, bool] = {}
        self.foundItem = None

    def ask_user_if_attribute(self, attribute):
        response = input(f"Is it true that {attribute}? (y/n): ").strip().lower()
        if response == 'y':
            self.inferredAttributes[attribute] = True
        elif response == 'n':
            self.inferredAttributes[attribute] = False

    def infer(self):
        possibleItems = self.items

        while len(possibleItems) > 1:
            possibleAttributes = {}
            for item in possibleItems:
                for attr in item.attributes:
                    if attr not in self.inferredAttributes:
                        possibleAttributes[attr] = True
            possibleAttributes = list(possibleAttributes)

            self.ask_user_if_attribute(possibleAttributes[0])

            for item in possibleItems[:]:
                for attribute in self.inferredAttributes:
                    if (self.inferredAttributes[attribute] == False and attribute in item.attributes) or (self.inferredAttributes[attribute] == True and attribute not in item.attributes):
                        possibleItems.remove(item)
                        break

        self.foundItem = possibleItems[0].name



# Example usage
if __name__ == "__main__":
    # Create an expert system
    es = ExpertSystem2()
    # Add rules
    #es.add_rule(Rule(["sunny"], "wear_sunglasses"))
    #es.add_rule(Rule(["rainy"], "take_umbrella"))
    #es.add_rule(Rule(["sunny", "weekend"], "go_to_beach"))
    es.items = [
        # Weapons
        Item("sword", ["sharp", "metal", "weapon", "melee"]),
        Item("dagger", ["sharp", "metal", "weapon", "melee", "light"]),
        Item("bow", ["weapon", "wooden", "ranged", "light"]),
        Item("crossbow", ["weapon", "metal", "ranged", "heavy"]),
        Item("axe", ["sharp", "metal", "weapon", "heavy"]),
        Item("staff", ["wooden", "magic", "weapon", "long"]),

        # Armor
        Item("shield", ["metal", "defensive", "heavy", "melee"]),
        Item("helmet", ["metal", "defensive", "headgear"]),
        Item("breastplate", ["metal", "defensive", "torso", "heavy"]),
        Item("boots", ["leather", "defensive", "footgear", "light"]),
        Item("gloves", ["leather", "defensive", "handgear", "light"]),

        # Consumables
        Item("health potion", ["liquid", "consumable", "magic", "healing"]),
        Item("mana potion", ["liquid", "consumable", "magic", "mana"]),
        Item("antidote", ["liquid", "consumable", "healing"]),
        Item("elixir", ["liquid", "consumable", "magic", "buff"]),

        # Tools
        Item("pickaxe", ["metal", "tool", "mining", "heavy"]),
        Item("shovel", ["metal", "tool", "digging", "heavy"]),
        Item("rope", ["tool", "light", "flexible"]),
        Item("lantern", ["tool", "light", "illumination"]),
        Item("compass", ["tool", "navigation", "small"]),

        # Misc / Magic
        Item("magic ring", ["magic", "wearable", "small"]),
        Item("amulet", ["magic", "wearable", "neckgear"]),
        Item("spellbook", ["magic", "consumable", "book", "heavy"]),
        Item("wand", ["magic", "weapon", "small", "ranged"]),
    ]

    # Perform inference
    es.infer()
    # Print final facts
    #print("Final facts:", es.facts)
    print(es.foundItem)