birds = ["eagle", "owl", "penguin", "albatross", "falcon"]

print("Which of the following birds can't fly:")
print(birds)

while input() != "penguin":
  print("wrong, guess again:")

print("Correct! Penguins can't fly 🐧")


tries = 0
print("Which of the following birds can't fly:")
print(birds)

while input() != "penguin":
  tries += 1
  print("wrong, guess again:")

  
  if tries >= 3:
    print("You have tried to many times, game over!")
    break

print("Correct! Penguins can't fly 🐧")
