import random
words = ["Programer","wow","man","women","redhead","black hat","ahahahahha"]
def word_gusser():
  word_to_guess =random.choice(words).lower()
  word_len= len(word_to_guess)
  guessed_word=["*"]*word_len
  attempts = 10
  guessed_letters = []

  while attempts > 0 and "*" in guessed_word:
    print(f"Word to guess: {' '.join(guessed_word)}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts Left: {attempts}")

    guess =input("Guess a letter:").lower()
    if len(guess) !=1 or not guess.isalpha():
      print("please enter a single valid letter.\n")
      continue
    if guess in guessed_letters:
      print("You already got that one ")
      continue

    guessed_letters.append(guess)
    if guess in word_to_guess:

      for i,letter in enumerate(word_to_guess):
        if letter ==guess:
          guessed_word[i]=guess
          print(f"Right at it {guess} is a right guess")
    else:
      attempts-=1
      print(f"sorry {guess} is not correct you lost one attempt")

  if '*' not in guessed_word:
    print(f"Congrats you won!")
  else:
    print(f"Game over!")

word_gusser()
