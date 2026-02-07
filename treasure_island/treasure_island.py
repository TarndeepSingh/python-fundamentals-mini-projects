"""
Project: Treasure Island
Description: A simple text-based adventure game where the player makes
choices to find the hidden treasure. This project practices conditional
logic and user input handling.
"""

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

# First choice
choice1 = input(
    'You are at a crossroad. Where do you want to go?\n'
    'Type "left" or "right":\n'
).strip().lower()

if choice1 == "left":

    # Second choice
    choice2 = input(
        '\nYou have come to a lake. There is an island in the middle of the lake.\n'
        'Type "wait" to wait for a boat.\n'
        'Type "swim" to swim across:\n'
    ).strip().lower()

    if choice2 == "wait":

        # Third choice
        choice3 = input(
            '\nYou arrive at the island unharmed.\n'
            'There is a house with 3 doors: red, yellow, and blue.\n'
            'Which color do you choose?\n'
        ).strip().lower()

        if choice3 == "red":
            print("\nIt\'s a room full of fire. Game Over 🔥")
        elif choice3 == "yellow":
            print("\nYou found the treasure. You Win! 🏆")
        elif choice3 == "blue":
            print("\nYou enter a room of beasts. Game Over 🐍")
        else:
            print("\nThat door doesn’t exist. Game Over.")

    else:
        print("\nYou got attacked by an angry trout. Game Over 🐟")

else:
    print("\nYou fell into a hole. Game Over 🕳️")

