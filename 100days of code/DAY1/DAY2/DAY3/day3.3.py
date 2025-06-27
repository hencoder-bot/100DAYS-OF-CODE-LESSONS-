#Nested if statements and elif statements
print('Welcome to the rollercooaster! ')
height = int(input('What is your height in cm?  '))

if height >= 120:
    print('you can ride the rollercoaster!')
else:
    print('Sorry, you have to grow taller before you can ride.')
age = int(input('What is your age?  '))
if age <= 12:
    print('Please pay $5')
elif age<= 18:
    print('please pay $7. ')
else:
    print('Please pay $12.')

