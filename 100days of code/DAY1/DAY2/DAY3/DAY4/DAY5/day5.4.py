#ADDING EVEN NUMBERS
#You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

#i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

#Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.
even_sum = 0
for num in range(0,10,2):
    even_sum=even_sum + num
print(f'the total even number of 0 to 10 is {even_sum}')


even_sum = 0
max_num = int(input('Enter your favourite even number \n'))
for num in range(0,max_num,2):
    even_sum=even_sum + num
print(f'the total even number of 0 to {max_num} is {even_sum}')

total = 0
for number in range(1,101):
    total += number
print(total)

#corretions
total = 0
for number in range(2, 101, 2):
    total += number
print(total)


total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
    #print(total2)--> shows total step by step
print(total2)

