import random
rock = """     
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""
paper="""   
     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.___(___)
"""
scissors = """  
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          """
game_images = [rock,paper,scissors]
user_choise = int(input("What do you choose? Type 0 for rock,1 for paper or 2 for scissors.\n"))
print(game_images[user_choise])
computer_choice =  random.randint(0,2)   
print('computer_choise:')
print(game_images[computer_choice])
if user_choise >= 3 or user_choise< 0:
      print('You typed an invalid number, you lose')
elif user_choise==0 and computer_choice==2:
      print('You win!')
elif computer_choice ==0 and user_choise==2:
      print('You lose!')
elif computer_choice > user_choise:
      print('You lose!')
elif user_choise > computer_choice:
      print('You win!')
elif computer_choice == user_choise:
      print('Its a draw!')

   
else:
      print('You typed a wronged number, You lose!')

