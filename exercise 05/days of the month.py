""""
Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

"""


year_month={'1':'31',          #Jan
      '2':'28',          #Feb
      '3':'31',          #Mar 
      '4':'30',          #Apr
      '5':'31',          #May
      '6':'30',          #Jun
      '7':'31',          #July
      '8':'31',          #Aug
      '9':'30',          #Sept
      '10':'31',         #Oct
      '11':'30',         #Nov
      '12':'31'          #Dec
            }         

monthnumber1=int(input("enter a month from (1-12): "))
if 1<=monthnumber1<=12:
      print(f"It has {year_month.get(str(monthnumber1))} days ")
else:
     print("enter a valid month number.")       