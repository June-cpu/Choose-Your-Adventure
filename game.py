class Adventurer:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def lose_health(self, amount):
        self.health -= amount
        print(f"{self.name} lost {amount} health. Current health: {self.health}")
        if self.health <= 0:
            print(f"{self.name} has no health left! Game over.")
            exit()

    def gain_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} gained: {item}. Current inventory: {self.inventory}")

    def __str__(self):
        return f"Adventurer {self.name}, Health: {self.health}, Inventory: {self.inventory}"


import random

# Function to ask a riddle and confirm the answer from the user.
def ask_riddle(difficulty, riddle_data):
    riddle = random.choice(riddle_data[difficulty])  # Select a riddle based on difficulty.
    print(f"Riddle: {riddle['question']}")
    user_answer = input("Your answer: ").strip()

    print(f"Your answer: {user_answer}")
    print(f"Correct answer: {riddle['answer']}")

    while True:
        try:
            correct = int(input("Did you get it right? (1 for Yes, 0 for No): ").strip())
            if correct in [0, 1]:
                if correct == 1:
                    print("Great! You may proceed.")
                else:
                    print("That's okay! You'll get the next one.")
                break
            else:
                print("Invalid input. Please enter 1 for Yes or 0 for No.")
        except ValueError:
            print("Please enter a valid number (1 or 0).")



def start():
    print("Welcome to the space adventure!")
    name = input("Enter your adventurer's name: ")
    player = Adventurer(name)  

    planets = [ilavurs, shummoor, lulucia, vixia, arispade, icriss, galem, earth ]  

    for planet in planets:
        description, riddle_info = planet()  
        print(description)  
        difficulty = riddle_info["difficulty"]  

        ask_riddle(difficulty, riddles)  

        
        correct = int(input("Did you get it right? (1 for Yes, 0 for No): ").strip())
        if correct == 1:
            player.gain_item(f"{difficulty.capitalize()} Riddle Solved")
        else:
            player.lose_health(20) 

        print(f"Current status: {player}")
        print("Moving on to the next planet...")

    print(f"Congratulations, {player.name}! You've completed the journey!")
    print(f"Final status: {player}")


import random

def intro():
    description = r"""
    
     :
                       :
                       :
                       :
        .              :
         '.            :           .'
           '.          :         .'
             '.   .-" .  -.   .'                                   .'':
               '."          ".'                               .-""-.'         .---.          .----.        .-""-.
                :            :                _    _        ."     .' ".    ..."     "...    ."      ".    ."       ".
        .........            .........    o  (_)  (_)  ()   :    .'    :   '..:.......:..'   :        :    :         :   o
                :            :                              :  .'      :       '.....'       '.      .'    '.       .'
                 :          :                             .'.'.      .'                        `''''`        `'''''`
                  '........'                              ''   ``
                 .'    :   '.
               .'      :     '.
             .'        :       '.
           .'          :         '.
                       :
                       :
                       :
                       :
    
    
    """
    intro_text = (
        "Welcome to 'Astra Lost in Space'!\n"
        "In this text-based adventure game, you will join a group of friends stranded in space after a mysterious incident.\n"
        "You must explore various planets, solve riddles, and gather resources to survive and find a way back home.\n\n"
        "About the Anime:\n"
        "Astra Lost in Space follows a group of high school students who go on a camping trip in space.\n"
        "After an unexpected event, they find themselves on a journey across uncharted planets, facing numerous challenges.\n"
        "As they navigate through these strange worlds, they must rely on each other and their wits to survive.\n\n"
        "Are you ready to embark on this adventure? Let's begin!\n"
    )
    print(description)
    print(intro_text)
    

def ilavurs():
    
    description = (
        "Ilavurs is a lush, tropical planet filled with giant vegetation and diverse animal life. "
        "After being stranded, the crew lands here seeking shelter and resources. "
        "They explore the vibrant ecosystem but must also be cautious of the wildlife and potential dangers lurking within the dense foliage."
    )
    return description, {"difficulty": "easy", "riddle": random.choice(riddles["easy"])}

def shummoor():
   
    description = (
        "Shummoor is a harsh desert planet characterized by extreme temperatures and dangerous sandstorms. "
        "The crew faces difficulties finding water and shelter as they navigate the vast dunes. "
        "They must work together to survive the relentless environment and avoid getting lost in the storms."
    )
    return description, {"difficulty": "easy", "riddle": random.choice(riddles["easy"])}

def lulucia():
    description = (
        "Lulucia is an ice-covered planet with sub-zero temperatures and limited resources. "
        "The crew struggles to find warmth and sustenance in the freezing conditions. "
        "They must use their ingenuity and teamwork to survive while searching for a way to leave the icy wasteland."
    )
    return description, {"difficulty": "easy", "riddle": random.choice(riddles["easy"])}

def vixia():
    description = (
        "Vixia is a seemingly peaceful, forested planet rich with a variety of life forms. "
        "The crew initially finds it inviting, but they soon realize that the planet hides dangers among its lush landscapes. "
        "They must navigate the complex ecosystem while being mindful of the unknown threats that lurk in the shadows."
    )
    return description, {"difficulty": "normal", "riddle": random.choice(riddles["normal"])}

def arispade():
    description = (
        "Arispade is a mysterious planet with peculiar atmospheric effects that disrupt communication and navigation. "
        "The crew faces confusion and disorientation as they attempt to explore the planet. "
        "They must rely on their instincts and work closely together to overcome the challenges presented by the strange environment."
    )
    return description, {"difficulty": "normal", "riddle": random.choice(riddles["normal"])}

def icriss():
    description = (
        "Icriss is a volcanic planet known for its hazardous lava flows and frequent seismic activity. "
        "The crew must tread carefully to avoid the dangerous eruptions and navigate through the treacherous terrain. "
        "Their survival depends on quick thinking and effective communication to stay safe amid the planet's volatility."
    )
    return description, {"difficulty": "normal", "riddle": random.choice(riddles["normal"])}

def galem():
    description = (
        

        "Galem is a gas giant featuring floating land masses, making it challenging for the crew to find stable ground. "
        "As they explore, they encounter unique phenomena and must be cautious of the unpredictable weather patterns. "
        "The crew's ability to adapt and think creatively is put to the test as they navigate the obstacles of this unusual world."
    )
    return description, {"difficulty": "hard", "riddle": random.choice(riddles["hard"])}

def earth():
    description = (
        
		r"""

				_-o#&&*''''?d:>b\_
          _o/"`''  '',, dMF9MMMMMHo_
       .o&#'        `"MbHMMMMMMMMMMMHo.
     .o"" '         vodM*$&&HMMMMMMMMMM?.
    ,'              $M&ood,~'`(&##MMMMMMH\
   /               ,MMMMMMM#b?#bobMMMMHMMML
  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk
 ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L
|               |MMMMMMMMMMMMMMMMMMMMbMH'   T,
$H#:            `*MMMMMMMMMMMMMMMMMMMMb#}'  `?
]MMH#             ""*""*#MMMMMMMMMMMMM'    -
MMMMMb_                   |MMMMMMMMMMMP'     :
HMMMMMMMHo                 `MMMMMMMMMT       .
?MMMMMMMMP                  9MMMMMMMM}       -
-?MMMMMMM                  |MMMMMMMMM?,d-    '
 :|MMMMMM-                 `MMMMMMMT .M|.   :
  .9MMM[                    &MMMMM*' `'    .
   :9MMk                    `MMM#"        -
     &M}                     `          .-
      `&.                             .
        `~,   .                     ./
            . _                  .-
              '`--._,dd###pp='

		
		"""
        "Earth is the final destination for the crew, a place of familiarity and comfort. "
        "After their long journey, they are finally home. "
		"Enjoy one last riddle"
    )
    return description, {"difficulty": "hard", "riddle": random.choice(riddles["hard"])}


riddles = {
    "easy": [
            {"question": "What has keys but can't open locks?", "answer": "Piano"},
            {"question": "What gets wetter as it dries?", "answer": "Towel"},
            {"question": "What has to be broken before you can use it?", "answer": "Egg"},
            {"question": "I'm tall when I'm young, and I'm short when I'm old. What am I?", "answer": "Candle"},
            {"question": "What has one eye, but can't see?", "answer": "Needle"},
            {"question": "What has hands but can't clap?", "answer": "Clock"},
            {"question": "What has a neck but no head?", "answer": "Bottle"},
            {"question": "Where does today come before yesterday?", "answer": "Dictionary"},
            {"question": "What belongs to you but others use it more than you do?", "answer": "Your name"},
            {"question": "What has many teeth but can't bite?", "answer": "Comb"},
            {"question": "What runs but never walks?", "answer": "River"},
            {"question": "What comes down but never goes up?", "answer": "Rain"},
            {"question": "What goes up and down but doesn't move?", "answer": "Stairs"},
            {"question": "What has a heart that doesn't beat?", "answer": "Artichoke"},
            {"question": "What is full of holes but still holds water?", "answer": "Sponge"},
            {"question": "What has a face and two hands but no arms or legs?", "answer": "Clock"},
            {"question": "What can you catch but not throw?", "answer": "Cold"},
            {"question": "What kind of band never plays music?", "answer": "Rubber band"},
            {"question": "What gets bigger the more you take away?", "answer": "Hole"},
            {"question": "What's black and white and read all over?", "answer": "Newspaper"},
            {"question": "What has stripes but isn't a tiger?", "answer": "Zebra"},
            {"question": "What begins with T, ends with T, and has T in it?", "answer": "Teapot"},
            {"question": "What has a thumb and four fingers but isn't alive?", "answer": "Glove"},
            {"question": "What month has 28 days?", "answer": "All months"},
            {"question": "What can you keep after giving it to someone?", "answer": "Your word"},
            {"question": "What has a ring but no finger?", "answer": "Telephone"},
            {"question": "What has wheels and flies but is not an airplane?", "answer": "Garbage truck"},
            {"question": "What has ears but cannot hear?", "answer": "Corn"},
            {"question": "What's orange and sounds like a parrot?", "answer": "Carrot"},
            {"question": "What has a bed but never sleeps?", "answer": "River"},
            {"question": "What has roots that nobody sees?", "answer": "Mountain"},
            {"question": "What can travel around the world while staying in a corner?", "answer": "Stamp"},
            {"question": "What has an end but no beginning?", "answer": "Stick"},
            {"question": "What has four fingers and a thumb but isn't alive?", "answer": "Glove"},
            {"question": "What kind of coat is best put on wet?", "answer": "A coat of paint"},
        ],
        
    "normal": [
            {"question": "The more you take, the more you leave behind. What am I?", "answer": "Footsteps"},
            {"question": "What has cities, but no houses; forests, but no trees; and rivers, but no water?", "answer": "Map"},
            {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "The letter M"},
            {"question": "Forward I am heavy, but backward I am not. What am I?", "answer": "Ton"},
            {"question": "What has a head, a tail, is brown, and has no legs?", "answer": "Penny"},
            {"question": "I am always hungry, I must always be fed. The finger I touch will soon turn red. What am I?", "answer": "Fire"},
            {"question": "What can fill a room but takes up no space?", "answer": "Light"},
            {"question": "I have keys but open no locks. I have space but no room. You can enter, but can't go outside. What am I?", "answer": "Keyboard"},
            {"question": "What is seen in the middle of March and April that can't be seen at the beginning or end?", "answer": "The letter R"},
            {"question": "What English word has three consecutive double letters?", "answer": "Bookkeeper"},
            {"question": "What 8-letter word can have a letter taken away and still make a word until only one letter is left?", "answer": "Starting"},
            {"question": "What five-letter word becomes shorter when you add two letters to it?", "answer": "Short"},
            {"question": "If two's company, and three's a crowd, what are four and five?", "answer": "Nine"},
            {"question": "What comes once in a year, twice in a month, four times in a week, and six times in a day?", "answer": "Odd numbers"},
            {"question": "What has six faces but does not wear makeup, has twenty-one eyes but cannot see?", "answer": "Dice"},
            {"question": "I have branches, but no fruit, trunk, or leaves. What am I?", "answer": "Bank"},
            {"question": "What can travel around the world while staying in a corner?", "answer": "Stamp"},
            {"question": "What has a thumb and four fingers but isn't alive?", "answer": "Glove"},
            {"question": "What is black when it's clean and white when it's dirty?", "answer": "Chalkboard"},
            {"question": "What has a neck and a body but no head?", "answer": "Bottle"},
            {"question": "What has a face and two hands but no arms or legs?", "answer": "Clock"},
            {"question": "What can you hold in your right hand but not in your left?", "answer": "Your left hand"},
            {"question": "What has teeth but cannot bite?", "answer": "Comb"},
            {"question": "What has an end but no beginning?", "answer": "Line"},
            {"question": "I'm light as a feather, yet the strongest man can't hold me for much longer than a minute. What am I?", "answer": "Breath"},
            {"question": "What can run but never walks, has a mouth but never talks?", "answer": "River"},
            {"question": "What is easy to get into, but hard to get out of?", "answer": "Trouble"},
            {"question": "I'm tall when I'm young, and I'm short when I'm old. What am I?", "answer": "Candle"},
            {"question": "What can you break, even if you never pick it up or touch it?", "answer": "Promise"},
            {"question": "What has many holes but still holds water?", "answer": "Sponge"},
            {"question": "What has roots that nobody sees?", "answer": "Mountain"},
            {"question": "What is it that lives if it is fed, and dies if you give it a drink?", "answer": "Fire"},
            {"question": "I have a tail and a head but no body. What am I?", "answer": "Coin"},
        ],
        
    "hard": [
            {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "answer": "Echo"},
            {"question": "I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?", "answer": "Fire"},
            {"question": "The person who makes it, sells it. The person who buys it never uses it. The person who uses it never knows they are using it. What is it?", "answer": "Coffin"},
            {"question": "I have branches, but no fruit, trunk, or leaves. What am I?", "answer": "Bank"},
            {"question": "What disappears as soon as you say its name?", "answer": "Silence"},
            {"question": "What has an eye but cannot see?", "answer": "Needle"},
            {"question": "The more you have of it, the less you see. What is it?", "answer": "Darkness"},
            {"question": "What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?", "answer": "River"},
            {"question": "If you drop me, I'm sure to crack, but give me a smile and I'll smile back. What am I?", "answer": "Mirror"},
            {"question": "I can be cracked, made, told, and played. What am I?", "answer": "Joke"},
            {"question": "I have keys but open no locks. I have space but no room. You can enter, but you can't go outside. What am I?", "answer": "Keyboard"},
            {"question": "What has a neck but no head?", "answer": "Bottle"},
            {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "The letter M"},
            {"question": "What has a bed but never sleeps?", "answer": "River"},
            {"question": "What is always in front of you but can't be seen?", "answer": "Future"},
            {"question": "What begins with T, ends with T, and has T in it?", "answer": "Teapot"},
            {"question": "What can fill a room but takes up no space?", "answer": "Light"},
            {"question": "What gets bigger the more you take away?", "answer": "Hole"},
            {"question": "What is always in front of you but can't be seen?", "answer": "Future"},
            {"question": "I am always hungry; I must always be fed. The finger I touch will soon turn red. What am I?", "answer": "Fire"},
            {"question": "What has teeth but cannot bite?", "answer": "Comb"},
            {"question": "What has a face and two hands but no arms or legs?", "answer": "Clock"},
            {"question": "What can you catch but not throw?", "answer": "Cold"},
            {"question": "I'm tall when I'm young, and I'm short when I'm old. What am I?", "answer": "Candle"},
            {"question": "What begins with T, ends with T, and has T in it?", "answer": "Teapot"},
            {"question": "What goes up but never comes down?", "answer": "Age"},
            {"question": "What has a bottom at the top?", "answer": "Legs"},
            {"question": "What is it that lives if it is fed, and dies if you give it a drink?", "answer": "Fire"},
            {"question": "What has a face and two hands but no arms or legs?", "answer": "Clock"},
            {"question": "What comes once in a year, twice in a month, four times in a week, and six times in a day?", "answer": "Odd numbers"},
    ]
}

start()