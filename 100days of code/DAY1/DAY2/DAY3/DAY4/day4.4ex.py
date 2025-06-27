# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(",")
# 🚨 Don't change the code above 👆
print(names)
#Write your code below this line 👇
import random
paying= random.choice(names)
print(paying)
print(f'mr {paying} will pay the bill')




#sample 2
str_inp =("opio,rogers,henry,oprohen")
op = str_inp.split(",")
print(op)
print('\n')
print('\n')
print('\n')

#corrections
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybodys names, separated by a comma. ")
names = namesAsCSV.split(",")
print(names)
num_items=(len(names))
random_choice=random.randint(0, num_items-1)
person_who_will_pay=names[random_choice]
print(f'{person_who_will_pay} is going to buy the meal')
