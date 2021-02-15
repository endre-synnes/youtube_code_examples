
mojito_ingredients = ["lime", "sugar", "mint leaves", "rum", "soda water", "ice"]

print("Name an ingredient in a Mojito:")

ingredient = input()

if ingredient in mojito_ingredients:
    print("Correct! " + ingredient + " is an ingredient in a mojito 🍹")
else:
    print("Wrong, there is no " + ingredient + " in a mojito")


