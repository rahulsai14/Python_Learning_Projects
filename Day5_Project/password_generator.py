import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the password Generator🙂')
num_letters = int(input('How many letters you want in your password? '))
num_digits = int(input('How many digits you want in your password? '))
num_symbols = int(input('How many symbols you want in your password? '))

password = ""

for i in range(0,num_letters):
    password += random.choice(letters)

for j in range(0,num_digits):
    password += random.choice(numbers)

for k in range(0,num_symbols):
    password += random.choice(symbols)

shuffled_password = list(password)
random.shuffle(shuffled_password)
new_password = ''.join(shuffled_password)
print(new_password)
