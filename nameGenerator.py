import numpy as np
randInt = np.random.randint
# the (somenting) of (something)
beginnings = ["Eye", "Crown", "Path", "Blood", "Fires", 
              "Hunt", "Shadow", "Lord", "Crossroads", "Knife", 
              "Towers", "Memory", "Heart", "Storm", "Shield", 
              "Legend", "Cavern", "Gate", "Rhythm", "Wheel", 
              "Cloud", "Shroud", "Wings", "Horn", "Chariot", 
              "Scroll", "Castle", "Kingdom", "River", "Desert", 
              "Ring", "Tomb", "City", "Prophecy", "Princess", 
              "Prince", "King", "Queen", "Raven", "Thieves", 
              "Assassin", "Oath", "Curse", "Warrior", "Heir",
              "Abyss", "Whisper", "Forest", "Blade", "Hour", 
              "Valley", "Flame", "Sancuary", "Voyage", "Word", 
              "Empire", "Chasm", "Serpent", "Protectors", "Guardian",
              "Demons", "Spirit", "Kingdom"]

endings = ["the World", "Heaven", "Chaos", "Swords", "Daggers",
           "Twilight", "Dreams", "Midnight", "Memory", "Light",
           "Dawn", "the Dragon", "War", "Fire", "Time", 
           "Darkness", "Glory", "Majesty", "Gold", "Anger", 
           "Deceit", "Stone", "Eternity", "Winter", "Ice", 
           "Crystal", "Mystery", "Secrets", "Enchantment", "Magic",
           "Destruction", "the Traitor", "the Earth", "Fools",
           "Lies", "Smoke", "Truth", "Glass", "Exile", 
           "Descent", "Scarcity", "Honor", "Dusk", "Ash"]

index1 = randInt(0, beginnings.__len__())
part1 = beginnings[index1]
index2 = randInt(0, endings.__len__())
part2 = endings[index2]

bookNum = index1 * endings.__len__() + index2 + 15

print("The Wheel Of Time Book %s: The %s of %s"%(bookNum, part1, part2))