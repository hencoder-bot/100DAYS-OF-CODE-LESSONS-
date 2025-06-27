#FIZZ BUZZ
#You are going to write a program that automatically prints the solution to the FizzBuzz game.
#Your program should print each number from 1 to 100 in turn.
#When the number is divisible by 3 then instead of printing the number it should print "Fizz".

for numbers in range(1,101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FIZZBUZZ")
    elif numbers % 3==0:
        print("FIZZ")
    elif numbers % 5 == 0:
        print("BUZZ")
    else:
        print(numbers)