print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to Treasure Island')
print('You need to find the treasure!!!')
decision1 = input('In which direction you want to go, Left or Right? ').lower()
if decision1 == "right":
    print('You have fallen into a pit')
else:
    decision2 = input('You have reached this level successfully and came across a river!! Now you want to "swim"ōr "wait" ').lower()
    if decision2 == "swim":
        print('You are eaten by a crocodile!! You are unable to find the treasure, Please try again')
    else:
        decision3 = input('You have successfully crossed the river!!, Now which door you want to go "Red", "Blue", "Yellow"? ').lower()
        if decision3 == "red":
            print('You have entered the room of flames!! Please try again')
        elif decision3 == "blue":
            print('You have entered the room full of water!! Please try again')
        elif decision3 == "yellow":
            print('Congratulations!! You found the treasure')

