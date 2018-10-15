#Fundementals, Question 3 Dice_Roll
from random import randint
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
