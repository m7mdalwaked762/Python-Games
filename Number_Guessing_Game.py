import random as r
def number_guessing_game():

  number_to_guess = r.randint(1,150)
  guesses_taken = 0
  max_gusses = 5
  Username = input("Hello there !, what is your name ?")
  print(f"Welcome to Number Randomizer Game {Username}!")
  print(f"You have {max_gusses} attempts.")
  while guesses_taken< max_gusses:
    try:
      guess =int(input("Enter Your Guess: "))
      guesses_taken +=1

      if guess < number_to_guess:
        print("Too low! Try again.")
      elif guess > number_to_guess:
        print("Too High! try again")
      else:
        print(f"congrat's you guessed the number{number_to_guess}")
        break
    except ValueError:
      print("Invalid Input :(")
  if guesses_taken==max_gusses:
    print(f"You've lost the number was {number_to_guess}")
number_guessing_game();
