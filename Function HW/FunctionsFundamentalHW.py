import math
print('1.')
num1=0
num2=0
extra=0
def mixnum(num1,num2,extra):
    while num1>num2 and num1>0:
        num1=num1-num2
        extra=extra+1
    print(extra,"(",num1,"/",num2,")")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
mixnum(num1, num2, extra)
print('-------------------------------------------')
print('2.')
vowels=0
def vowel_count1(word,vowels):
    for i in range (0,len(word)):
        if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u":
            vowels+=1
    print(vowels)
word=input("Type in a string value:")
vowel_count1(word,vowels)
print('-------------------------------------------')
print('3.')
va=0
ve=0
vi=0
vo=0
vu=0
def vowel_Num(word,va, ve, vi, vo, vu):
    for i in range (0,len(word)):
        if word[i]=="a":
            va+=1
        elif word[i]=="e":
            ve+=1
        elif word[i]=="i":
            vi+=1
        elif word[i]=="o":
            vo+=1
        elif word[i]=="u":
            vu+=1
    print("a =",va,"e =",ve,"i =",vi,"o =",vo,"u =",vu)
word=input("Type in a string value:")
vowel_Num(word,va, ve, vi, vo, vu)
print('-------------------------------------------')
print('4.')
vowel=[]
def vowel2(word):
    for i in range (0,len(word)):
        if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u":
            vowel.append(i+1)
    return vowel[0:]
word=input("Type in a string value:")
out=vowel2(word)
print(out)
print('-------------------------------------------')
print('5.')
radius=0
def SphereV(radius):
    r3=pow(radius,3)
    ans=round((4*math.pi)*(r3/3))
    print("The volume of the sphere is:",ans,"cm")
def SphereS(radius):
    r2=pow(radius,2)
    ans2=round((4*math.pi)*r2)
    print("The surface area of the sphere is:", ans2,"cm")
radius=int(input("Enter radius of sphere(cm):"))
SphereV(radius)
SphereS(radius)
print('-------------------------------------------')
print('6.')
radius=0
def SphereV(radius):
    r3=pow(radius,3)
    ans=round((4*math.pi)*(r3/3))
    return ans
def SphereS(radius):
    r2=pow(radius,2)
    ans2=round((4*math.pi)*r2)
    return ans2
def form(a1,a2,radius):
    print("Radius|4π(r^(2))|4π(r^(3))")
    print(radius,"    | ",a1,"   | ",a2)
radius=int(input("Enter radius of sphere(cm):"))
a1=SphereV(radius)
a2=SphereS(radius)
form(a1,a2,radius)
print('-------------------------------------------')
print('7.')
def person(name='(Not Entered)', age='(Not Entered)', weight='(Not Entered)'):
    print('Name:',name,"\nAge:",age,"\nWeight:",weight)
name=input("Your name (\"君の名は\"):")
age=input("Your age (\"Don't be shy\"):")
weight=input("Your weight(\"Don't worry I won't tell any one\"):")
person(name,age,weight)
print('-------------------------------------------')
print('8.')
def RGB(HexR, HexG, HexB):
    HexR=int(HexR, 16)
    HexG=int(HexG, 16)
    HexB=int(HexB, 16)
    print("Dean-",HexR,":",HexG,":",HexB)
def Hex(R,G,B):
    R=hex(int(R)).replace('0x', '')
    G=hex(int(G)).replace('0x', '')
    B=hex(int(B)).replace('0x', '')
    print("Hex-",R,":",G,":",B)
    
R=input("Enter value of Red:")
G=input("Enter value of Green:")
B=input("Enter value of Blue:")
Hex(R,G,B)
HexR=input("Enter hexidecimal value of Red:")
HexG=input("Enter hexidecimal value of Green:")
HexB=input("Enter hexidecimal value of Blue:")
RGB(HexR, HexG, HexB)
