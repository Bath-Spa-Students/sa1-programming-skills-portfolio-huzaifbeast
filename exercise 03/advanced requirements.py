"""
### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?


____________________

"""
#answer 
 

name1 = input("What is your first name?: ")
name2 = input("What is your second name?: ")
hometown = input("Where do you belong from?: ")

while True:
    age = input("Enter age: ")
    if age.isdigit():    
        Admin_info = {
            "name": f"{name1} {name2}",
            "hometown": hometown,
            "age": age
        }
        print(f"{Admin_info.get('name')}\n{Admin_info.get('hometown')}\n{Admin_info.get('age')}")
        break
    else:
        print("Please enter age in numbers.")
