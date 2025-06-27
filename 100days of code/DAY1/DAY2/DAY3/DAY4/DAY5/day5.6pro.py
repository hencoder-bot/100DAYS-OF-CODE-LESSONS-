#PASSWORD GENERATOR PROJECT(not using loops)
import random
#lettera = (input("Enter the alphabetical letters\n"))
#alphabets = lettera.split(",")
#print(alphabets)
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
           'x', 'y', 'z', '', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1','2', '3', '4', '5', '6', '7', '8', '9',]

symbols = ['!','"','#','$','%','&',
            "'",'(',')','*','+','', 
            ' ','-','.','/',':',';',
              '<','=','>','?','@', 
              '[','\\',']','^','_',
                '{''|','}',]

print('WELCOME TO THE PYPASSWORD GENERATOR')
no_letters = int(input("How many letters would you like your password to have? \n"))
no_symbols = int(input("How many symbols would you love your password to have? \n"))
no_numbers = int(input("How many numbers would you love your password to have? \n"))

import random
 # Generate two unique random numbers between 1 and 6
random_numbers = random.sample(numbers, no_numbers)
random_letters = random.sample(letters, no_letters )
random_symbols = random.sample(symbols ,no_symbols)
print(random_numbers)
print(random_letters)
print(random_symbols)
a=[random_letters,random_symbols,random_numbers]
print(a)
result =''.join(random_numbers)
print(result)
result2=''.join(random_letters)
print(result2)
result3=''.join(random_symbols)
print(result3)
pass1=(result+result2+result3)

pass1_list = list(pass1) 
random.shuffle(pass1_list) 
shuffled_pass1 = ''.join(pass1_list) 
print(f"your password is, {shuffled_pass1}")


#CORRECTIONS
#EASY LEVEL
import random
#lettera = (input("Enter the alphabetical letters\n"))
#alphabets = lettera.split(",")
#print(alphabets)
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
           'x', 'y', 'z', '', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1','2', '3', '4', '5', '6', '7', '8', '9',]

symbols = ['!','"','#','$','%','&',
            "'",'(',')','*','+','', 
            ' ','-','.','/',':',';',
              '<','=','>','?','@', 
              '[','\\',']','^','_',
                '{''|','}',]

print('WELCOME TO THE PYPASSWORD GENERATOR')
nr_letters = int(input("How many letters would you like your password to have? \n"))
nr_symbols = int(input("How many symbols would you love your password to have? \n"))
nr_numbers = int(input("How many numbers would you love your password to have? \n"))

password =""

for char in range(1, nr_letters+1):
   # random_char=random.choice(letters)
    #password += random_char
    #print(password)
  password += random.choice(letters)

for char in range(1,nr_symbols +1):
    password += random.choice(symbols)

for char in range(1,nr_numbers +1):
      password += random.choice(numbers)

print(password)

#the hard level
import random
#lettera = (input("Enter the alphabetical letters\n"))
#alphabets = lettera.split(",")
#print(alphabets)
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
           'x', 'y', 'z', '', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1','2', '3', '4', '5', '6', '7', '8', '9',]

symbols = ['!','"','#','$','%','&',
            "'",'(',')','*','+','', 
            ' ','-','.','/',':',';',
              '<','=','>','?','@', 
              '[','\\',']','^','_',
                '{''|','}',]

print('WELCOME TO THE PYPASSWORD GENERATOR')
nr_letters = int(input("How many letters would you like your password to have? \n"))
nr_symbols = int(input("How many symbols would you love your password to have? \n"))
nr_numbers = int(input("How many numbers would you love your password to have? \n"))

password_list = []

for char in range(1, nr_letters+1):
   # random_char=random.choice(letters)
    #password += random_char
    #print(password)
  password_list += random.choice(letters)

for char in range(1,nr_symbols +1):
    password_list.append(random.choice(symbols))

for char in range(1,nr_numbers +1):
      password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"your password is{password}")