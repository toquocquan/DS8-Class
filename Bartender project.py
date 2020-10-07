# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:12:16 2020

@author: FS120802
"""

import random

questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}
ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


Customer_response = ["YES", "OK","GOOD"]

print('Bartender: Hello Sir ! Wellcome to our NightClub :)) ')
for key in questions:
    batender_question=questions.get(key)
    print('Bartender:'+batender_question)
    customer_required=input("Customer: ")
    #print(customer_required.upper())
    if (customer_required.upper()) in Customer_response:
        wine_suggestion = ingredients.get(key)
        wine=random.choice(wine_suggestion)
        #print('Bartender: '+wine)
        print ("Bartender: Why don't you taste: " + wine.upper())
        customer_required=input("Customer: ")
        if (customer_required.upper()) in Customer_response   :
            print("Bartender: Thank you & enjoy your wine :) ")
            break
        break
    else:
        print("Bartender: Goodbye & see you next time :D ")

