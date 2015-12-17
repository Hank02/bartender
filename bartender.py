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

def maker(likes):
    drink = []
    for each in likes:
        if preferences[each] == True:
            drink.append(random.choice(ingredients[each]))
    return drink

if __name__ == '__main__':
    ask_user()
    maker(preferences)