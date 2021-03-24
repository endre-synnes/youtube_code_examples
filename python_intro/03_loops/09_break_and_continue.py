from random import randrange
import time

birds = ["eagle", "owl", "penguin", "albatross", "falcon"]

correctGuess = "penguin"



while True:
  index = randrange(5)

  print(f"New guess: {birds[index]}")
  time.sleep(2)

  if birds[index] == correctGuess:
    break



print(f"Correct! The answer was {correctGuess}")
