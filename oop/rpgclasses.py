import pdb

class Character:
    
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
        
class NPC(Character):
    
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
    
    def speak(self, text="text goes hear"):
        self.text = text
        return self.text

villager = NPC("Bob", 100, 12)
print(villager.name)
print(villager.hp)
print(villager.level)
print(villager.speak())

pdb.set_trace()