import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

choice = int(input('Type 0 for rock, 1 for paper, 2 for scissors: '))
if choice >=3 and choice<0:
    print('Invalid Choice, please select the right choice')
else:
    list_elements = [rock,paper,scissors]
    print('You choose: ')
    print(list_elements[choice])

    computer_choice = random.randint(0,2)
    print('Computer Choose: ')
    print(list_elements[computer_choice])

    if choice == 0 and computer_choice == 2:
        print('You won')
    elif computer_choice == 0 and choice == 0:
        print('Computer won')
    elif choice > computer_choice:
        print('You won')
    elif computer_choice > choice:
        print('Computer won')
    elif computer_choice == choice:
        print('Draw')


#Alternative Logic
'''
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print('Choose one of the options above!!')

print('Computer choice: ')

if random_choice == rock:
    print(random_choice)
    if choice == 0:
        print('Draw')
    elif choice == 1:
        print('User won')
    else:
        print('Computer won')

if random_choice == paper:
    print(random_choice)
    if choice == 0:
        print('Computer wins')
    elif choice == 1:
        print('Draw')
    else:
        print('User won')

if random_choice == scissors:
    print(random_choice)
    if choice == 0:
        print('User wins')
    elif choice == 1:
        print('Computer wins')
    else:
        print('Draw')
'''
