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

#Write your code below this line 👇
image_ = [rock,paper,scissors]
user_choice = int(input("What do you want to choose 🤔? 0 for Rock, 1 for Paper, 2 for Scissor\n"))
if user_choice >= 3 or user_choice < 0 :
  print("Invalid number , You lose")
else:
  print(f"Your choice is {user_choice}")
  print(image_[user_choice])
  
  computer_choice = random.randint(0,2)
  print(f"Computer choice is {computer_choice}")
  print(image_[computer_choice])
  
  
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif user_choice == 2 and computer_choice == 0: 
    print("You lose")
  elif user_choice > computer_choice :
    print("You win!")
  elif computer_choice > user_choice:
    print("Ypu lose")
  elif computer_choice == user_choice:
    print("You draw")
