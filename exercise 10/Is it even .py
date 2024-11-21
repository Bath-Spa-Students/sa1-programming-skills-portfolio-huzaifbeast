"""
Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.

"""

#answer

def cheaking(value):
    if value % 2==0:
        return(f"{value} is an even number")   # for even number
    else:
        return(f"{value} is an odd number")    # for odd number

def main():
    for_user = input("Enter a number: ")
    value = int(for_user)
    result = cheaking(value)
    print(result)    
main()    