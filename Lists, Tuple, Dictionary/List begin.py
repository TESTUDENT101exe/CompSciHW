import random
import math
Index=[0,1,2,3]
Element=["a", "z", "d", "g"]

RandoList=[]
elelist=[]
diction={"a":"","b":"","c":"","d":"","e":""}
key=["a","b","c","d","e"]
var1=0
'''
var1=Element[Index[var1-1]]
Element[3]=Element[Index[0]]
Element[0]=var1
print(Element)


var=Index[1:3]
Index+=var
Index.insert(0,var)
print(Index)

for i in range(0,4):
    for j in range(0,5):
        print(Index[i], end="")


while len(RandoList)!=99:
    num=random.randint(0,1000000000)
    if num%2==1 and num%7!=0:
        RandoList.append(num)
print(RandoList[0:])

for i in range(0,5):
    rand=random.randint(0,100)
    diction[key[i]]=rand
for i in range(0,5):
    print(diction[key[i]],end=",")
'''
