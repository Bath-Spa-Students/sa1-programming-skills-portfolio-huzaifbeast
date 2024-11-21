"""
Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case.
* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.
*You may include all loops in a single project*

"""

#answer

no1=0
while no1 <=50:
    print(no1)
    if no1==50:
        break    # to stop the loop
    no1 +=1

no2=50
while no2 >=0:
    print(no2)
    if no2==0:
        break   # to stop the loop
    no2 -=1
no3=30
while no3 <=50:
    print(no3)
    if no3==50:
        break   # to stop the loop
    no3 +=1

no4=50
while no4 >=10:
    print(no4)
    if no4==10:
        break   # to stop the loop
    no4 -=2

no5=100
while no5<=200:
    print(no5)
    if no5==200:
        break   # to stop the loop
    no5 +=5             
