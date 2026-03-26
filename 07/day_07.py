#today we will do hangman since i noticed i havemt explained in the others what eatch day does i will add a text file to the project all together to see what each day does as a discription file 
import random


words = [
    "apple", "apricot", "abruptly", "absurd", "abyss", "affix", "askew", "avenue", 
    "awkward", "axiom", "azure", "breeze", "baggage", "bandwagon", "banjo", 
    "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", 
    "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", 
    "buzzing", "buzzwords", "cactus", "caliph", "cobweb", "cockiness", "croquet", 
    "crypt", "curacao", "cycle", "dragon", "dizzying", "duplex", "dwarves", 
    "eclipse", "embezzle", "equip", "espionage", "exodus", "falcon", "faking", 
    "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", 
    "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "geyser", 
    "gabby", "galaxy", "galvanize", "gazing", "giaour", "gizmo", "glowworm", 
    "glyph", "gnarly", "gnostic", "gossip", "grogginess", "hazard", "haiku", 
    "haphazard", "hyphen", "igloo", "iatrogenic", "icebox", "injury", "ivory", 
    "ivy", "jungle", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", 
    "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", 
    "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kite", "khaki", 
    "kayaking", "kazoo", "keyhole", "kilobyte", "kiosk", "kitsch", "lunar", 
    "luxury", "lymph", "magnet", "matrix", "mystify", "nebula", "nightclub", 
    "nowadays", "orchard", "oxidize", "oxygen", "python", "pajama", "pixel", 
    "puzzling", "quartz", "queue", "quips", "quixotic", "rhythm", "razzmatazz", 
    "rhubarb", "sphinx", "scratch", "snazzy", "stymied", "thrift", "topaz", 
    "twelfth", "unzip", "utopia", "unknown", "unworthy", "vortex", "vaporize", 
    "vixen", "wizard", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", 
    "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "xenon", 
    "xylophone", "yacht", "yippee", "yoked", "youthful", "zephyr", "zigzag", 
    "zigzagging", "zilch", "zipper", "zodiac", "zombie"
]

word  = random.choice(words)

placeholder = ''
for i in range(len(word)):
    placeholder += '_'
lives = 8
#print(word)
new_list = list(word)

print(placeholder)
current = list(placeholder)
def finished():
    if "".join(current) != word and lives > 0:
        return True
    else:
        return False
        
while finished():
    found = True
    guess = input("Guess a word :")
    for letter in word:
       if(guess == letter):
           for i in range(0,len(new_list)):
               if(guess == new_list[i]):
                   current[i] = guess
           print("".join(current))
           found = False
           
        
    if(found):
        lives -=1
    print(lives)
    

        



