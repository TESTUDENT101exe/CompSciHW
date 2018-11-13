from random import randint

#Fundementals, Question 1 While and For loop
counta=8
countb=8
def whileFor(counta, countb):
    print("While Loop")
    while counta!=-4:
        print(counta)
        counta=counta-1
    print("For Loop")
    for i in range(0,12):
        print(countb-i)

#Fundementals, Question 2 is_odd
def is_odd():
    for i in range(1,10):
        if i%2==1:
            print("True:",i)
        else:
            print("False",i)


#Fundementals, Question 3 Dice_Roll
def Dice_Roll():
    results=[]
    reroll=0
    rolls="QWERTY"
    def DiceRoller(rolls):
        for i in range(0,rolls):
            out=randint(1,6)
            results.append(out)

        print("The results from rolling the dice are:",results[0:])
    while reroll!="n":
        while rolls.isdigit()==False:
            try:
                int(rolls)
            except ValueError:
                rolls=input("Enter the number of times you want to roll the dice:")
        rolls=int(rolls)
        DiceRoller(rolls)
        while reroll!="y" and reroll!="n":
            reroll=input("Do you want to roll again (y/n):")
        if reroll=="y":
            reroll=0
            rolls="QWERTY"
            del results[0:]

#Fundementals, Question 4 OddEven
number='155438002857'
def OddEven(number):
    odd=0
    even=0
    for i in number:
        if int(i)%2==1:
            odd+=1
        else:
            even+=1
    print("Odd:",odd,'\nEven:',even)


#whileFor(counta, countb)
#is_odd()
#Dice_Roll()
#OddEven(number)