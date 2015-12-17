import random

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? ",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

adjectives = [
    "Bohemian",
    "Caribbean",
    "Lonely",
    "Angry",
    "Mexican",
    "Rebelious",
    "Stincky",
    "Deadly",
    "Painful",
    "Regretful",
    "Filthy",
    "Faithful",
]

nouns = [
    "Cat",
    "Dog",
    "Tiger",
    "Rat",
    "Cockroach",
    "Hammer",
    "Slap",
    "Fist",
    "Stool",
    "Boot",
    "Curse",
    "Storm",
]

# create dictionary to store customer preferences
preferences = {}

# function to ask cutomer preferences
def ask_user():
    for key in questions:
        answer1 = input(questions[key])
        answer2 = False
        if answer1 == "yes" or answer1 == "YES" or answer1 == "Yes" or answer1 == "yEs" or answer1 == "yeS" or answer1 == "y":
            answer2 = True
        preferences[key] = answer2

# function that combines ingrediantes based on customer preferences
def maker(likes):
    drink = []
    for each in likes:
        if preferences[each] == True:
            drink.append(random.choice(ingredients[each]))
    return drink

# function that names drink
def namer():
    title = random.choice(adjectives) + " " + random.choice(nouns)
    return title
    
if __name__ == '__main__':
    more = True
    while more:
        ask_user()
        drink = maker(preferences)
        drinkname = namer()
        print("\n")
        print("Here is the recipe for your {}:".format(drinkname))
        for n in drink:
            print("   A {}".format(n))
        print("\n")
        response = input("Another one? ")
        if response == "yes" or response== "YES" or response == "Yes" or response == "yEs" or response == "yeS" or response == "y": 
            more = True
        else:
            more = False
            print("Bye, then...")
