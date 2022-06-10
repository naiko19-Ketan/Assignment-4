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
