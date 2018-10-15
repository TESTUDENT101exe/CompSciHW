import math
from random import random, randint
import random
'''
def age(page):
    if int(page)<18:
        print("THIS PERSON IS NOT OLD ENOUGH TO DRIVE")
    else:
        print("Drive safely")
page=input("Enter your age:")
age(page)
'''
'''
def tri(a1,a2,a3):
    if a1=90 or a2=90 or a3=90:
        print("This is a right angle triangle")
    elif a1=60 and a2=60 and a3=60:
        print("This is a equalatrual triangle")
    elif  a1>90 or a2>90 or a3>90:
        print("This is a obtuse triangle")
    elif  a1<40 or a2<40 or a3<40:
        print("This is a obtuse triangle")
    else:
        print("This is not a triangle")
a1=int(input("Enter First Angle"))
a2=int(input("Enter Second Angle"))
a4=int(input("Enter Third Angle"))
tri(a1,a2,a3)
'''
'''
num=90
def FIZZBUZZ(num):
    if num%3==0 and num%5==0:
        print("FIZZ BUZZ")
    elif num%5==0:
        print("BUZZ")
    elif num%3==0:
        print("FIZZ")
    else:
        print("HUH?")
FIZZBUZZ(num)
'''
def nCr(n,r):
    f = math.factorial
    return nCr2(f(n) / f(r) / f(n-r)),f(n) / f(r) / f(n-r)

def nCr2(n):
    if n>1000000:
        print("Impossible")
    elif n<1000000 and n>10000:
        print("You have a chance")
    else:
        print("Possible!")

print(nCr(24,2))
'''
#print(random(10))
#print(randint(69,420))
def Somethinginator():
    inum=random.randint(1,10)
    if inum==1:
        print("Very good you just barely avoided failing")
    elif inum==2:
        print("MERDE!")
    elif inum==3:
        print("mha hart, mah sole!")
    elif inum==4:
        print("Touche Trebuche")
    elif inum==5:
        print("Meh")
    elif inum==6:
        print("{-}7")
    elif inum==7:
        print("Mister Stark, I don't feel so good")
    elif inum==8:
        print("Stalin Aproves!")
    elif inum==9:
        print("NSWF")
    elif inum==10:
        print("SWF")
    print(inum)
Somethinginator()
'''
'''
right=0
roll=[]
guess=[3,5,6]
for i in range(0,3):
    ranum=random.randint(1,6)
    roll.append(ranum)
for f in range(0,3):
    if guess[i]==roll[i]:
        right+=1
print("You guessed", right, "correctly")
'''
