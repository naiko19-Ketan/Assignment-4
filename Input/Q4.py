print("Q1")
marks=int(input("Enter your marks(0 to 100): "))
if marks>=80:
    print("A")
elif marks>=60 :
    print("B")
elif marks>=50 :
    print("C")
elif marks>=45:
    print("D")
elif marks>=25 :
    print("E")
else  :
    print("F")
print("Q2")
year=int(input("Enter the year : "))
if year%400 == 0 and year%100==0 :
    print("{} is a leap year".format(year)) 
elif  year%4==0 and year%100 != 0:
    print("{} is a leap year".format(year))
else :
    print("{} is not a leap year".format(year))
print("Q3")
import random


for num in range(1,11):
    number1 = random.randint(2,15)
    number2 = random.randint(2,15)
    answer = number1 * number2

    print ("Question",num,":What is", number1, "x", number2, "?")
    guess=int(input())    

    if guess!=answer :
        print("Wrong.The right answer is",answer)
    else :
        print("Right!")
print("Q4")

for candies in range(1,201):
    if (candies % 5 != 2):
        continue
    if (candies % 6 != 3):
        continue
    if (candies % 7 != 2):
        continue

    print(str(candies) + " is the answer!")
    break
