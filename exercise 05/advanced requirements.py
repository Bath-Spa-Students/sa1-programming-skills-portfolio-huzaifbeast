"""
### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.

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

leap_month= {"2":"FEb"}
monthnumber1=int(input("enter a month from (1-12): "))
if 1<=monthnumber1<=12:
      if monthnumber1==2:
            month_feb=input("Is it a leap year(yes/no): ")
            if month_feb== "yes":
                  print(f"{leap_month.get(str(monthnumber1))} has 29 days in it")
            elif month_feb=="no":
                  print(f"{leap_month.get(str(monthnumber1))} ")
            else:
                  print("enter yes/no ")   # if inout is diff   

      print(f"It has {year_month.get(str(monthnumber1))} days ")
else:
     print("enter a valid month number.")       