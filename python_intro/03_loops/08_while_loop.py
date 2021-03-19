birds = ["eagle", "owl", "penguin", "albatross", "falcon"]

counter = 0

while counter < len(birds):
  print(f"How are you ms {birds[counter]}?")
  counter += 1


counter = 0

while True:
  if counter >= 5:
    break

  print(f"hello nr {counter}")

  counter += 1

