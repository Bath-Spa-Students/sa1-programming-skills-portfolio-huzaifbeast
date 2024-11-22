"""
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza.

"""


#ANSWER

#using loop to ask user for pizza toppings
while True:
    pizza=input("please input the toppings u want and type 'quit' when u finished ")
    
    if pizza.lower()=="quit":

        break              # to stop the loop if the user typed quit

    print(f"{pizza}  will be added to your pizza as a toppings of your choice.")