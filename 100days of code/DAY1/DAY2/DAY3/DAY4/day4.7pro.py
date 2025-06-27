
#ROCK PAPER SCISSORS GAME
#BY OPROHEPYTHONZ

choises = input("Which number do you want to choose 0 for rock,1 for paper,2 for scissors: \n");"0","1","2"

if choises=="0":
     print("""   
     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.___(___)
""")
elif choises=="1":
     print("""     
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

""")
elif choises=="2":
     print("""  
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          """)
     
#for computer
import random
choises2=[0,1,2]
computer = random.choice(choises2)
print(computer)
if computer== 0:
     print("""   
     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.___(___)
""")
elif computer== 1:
     print("""     
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

""")
elif computer== 2:
     print("""  
  _______
---'   ____)____
          ______)
       __________)
      (____)jju
---.__(___)
          """)
if choises=="0" and computer==0:
 print('🤝🤝🤝Its a draw')
elif choises=="1" and computer==1:
 print('🤝🤝🤝Its a draw')
elif choises=="2"and computer==2:
 print('🤝🤝🤝It a draw')
elif choises=="2" and computer==1:
 print('💪💪💪Congrajulations, you win')
elif choises=="0" and computer==1:
 print('💪💪💪Congrajulations, you win')
elif choises=="0" and computer==2:
 print('💪💪💪Congrajulations, you win')
else:
   print('😭😭😢Sorry, You lost.good luck next time')


   #CORRECTIONS
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
   user_choise = int(input("What do you choose? Type 0 for rock,1 for paper or 2 for scissord."))
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

