import random
# Defining Rock, Paper, and Scissors
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
# A prompt to emulate the users choice of 0 ,1 or 2
userChoice=int(input("what do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# A if stamtment to make sure the user gives the right input
if userChoice==0 or userChoice==1 or userChoice==2:

# three if stamnets to display users output
  if userChoice==0:
      print(rock)
  if userChoice==1:
      print(paper)
  if userChoice==2:
      print(scissors)

#emulating the computers choice and displaying it
  gameChoice=["rock","paper","scissors"]
  computerChoice = random.choice(gameChoice)
  print("computer choice:")
  if computerChoice =="rock":
            print(rock)
  if computerChoice =="paper":
            print(paper)
  if computerChoice =="scissors":
            print(scissors)

# game logic and if statments to detrmine who is the winner
  if userChoice==0 and computerChoice=="paper":
            print("you lost")
  if userChoice==0 and  computerChoice=="rock":
            print("draw")
  if userChoice==0 and  computerChoice=="scissors":
            print("you won !")
  if userChoice==1 and computerChoice=="paper":
            print("draw")
  if userChoice==1 and  computerChoice=="rock":
            print("you won !")
  if userChoice==1 and  computerChoice=="scissors":
            print("you won !")
  if userChoice==2 and computerChoice=="paper":
            print("you won !")
  if userChoice==2 and  computerChoice=="rock":
            print("you lost")
  if userChoice==2 and  computerChoice=="scissors":
            print("draw")
else:
  print("invalid input, please try again")
