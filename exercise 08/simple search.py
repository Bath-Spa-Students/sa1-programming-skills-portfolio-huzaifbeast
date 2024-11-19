"""
Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.



"""

#answer 

kids=("Jake", "Zac", "Ian", "Ron", "Sam", "Dave") # the list of kids 

tosearch=input("enter the name u want to search: ")    #to find a specific child name

#using if else statement to search if child is in the list or not

if tosearch in kids:
    print(f"{tosearch} is in the list")
else:
    print(f"{tosearch} not in the list")    


