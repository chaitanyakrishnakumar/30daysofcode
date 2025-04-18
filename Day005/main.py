import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Easy Level: elements in sequence
password_list = []
for letter in range(nr_letters):
    smtg = random.choice(letters)
    password_list.append(smtg)

for symbol in range(nr_symbols):
    smtg = random.choice(symbols)
    password_list.append(smtg)

for number in range(nr_numbers):
    smtg = random.choice(numbers)
    password_list.append(smtg)

# easy_password = ""
# for item in password_list:
#     easy_password += item
# print(f"Your easy password is: {easy_password}")

# Hard Level: shuffling elements 
hard_password = ""
random.shuffle(password_list)
for item in password_list:
    hard_password += item
print(f"Ta-da! Your new password: {hard_password}")
