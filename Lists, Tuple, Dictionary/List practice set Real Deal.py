import random
#f001 Parts
list1=[1, 1, 13, 4, 5]
count=0
#f002 Parts
list2=[0, 1, 4, 5, 10, 8, 7]
addup=0
#f003 Parts
list3=[7, 4, 5, 5, 4, 7]
#f004 Parts
list4=["HI", "hi", "bye", "bye", "f"]
#f005,f006 Parts
xyz=[1, 1, 1]
xyz2=[1, 1, 1]
cordsection=[]
coords=[]
diffxyz=[200, 200, 200]
newdiffxyz=[0,0,0]
xyz = [200, 200, 200]
xyz2 = [200, 200, 200]
#f007 Parts
integer=[]
morethan20=[]

def f001(list1,count):
    if len(list1)==0:
        print(0)
    else:
        for i in range(len(list1)):
            if list1[i]!=13 and list1[i-1]!=13:
                count+=list1[i]
        print("1)",count)

def f002(list2,addup):
    for i in range(len(list2)):
        if i!=0 and i!=len(list2)-1:
            addup+=list2[i]
    addup=int(addup/(len(list2)-2))
    print("2)",addup)

def f003(list3):
    if list3==list3[::-1]:
        print("3)",True)
    else:
        print("3)",False)

def f004(list4):
    for i in range(len(list4)-1):
        for j in range(i+1,len(list4)-1):
            if list4[i]==list4[j]:
                list4.remove(list4[j])
            elif list4[i]==list4[j].upper():
                list4.remove(list4[j])
    print("4)",list4[0:])

def f005(coords,cordsection):
    for i in range(1000):
        del cordsection[0:]
        for j in range(3):
            cord=random.randint(-100,101)
            cordsection.append(cord)
        coords.append(tuple(cordsection[0:]))
    #print('Co-ordinate list:',coords)
    print(f006(coords, diffxyz, newdiffxyz, xyz, xyz2))

def f006(coords, diffxyz, newdiffxyz, xyz, xy2):
    for i in range(len(coords)-1):
        closer=0
        for l in range(i+1,len(coords)-1):
            for j in range(3):
                if i+1<=len(coords) and j+1<3:
                    newdiffxyz[j]=abs(coords[i][j])-abs(coords[l][j+1])
            for k in range(3):
                if newdiffxyz[k]<=diffxyz[k]:
                    closer+=1
                    diffxyz[k]=newdiffxyz[k]
            if closer>1:
                xyz=coords[i]
                xyz2=coords[l]
    return "5) Co-ordinate 1:", xyz,"Co-ordinate 2:", xyz2

def f007(integer):
    for i in range(100):
        newnum=random.randint(0,1000)
        integer.append(newnum)
    integer.sort()
    for j in range(0,len(integer)-1):
        if (j-1)!=-1 or j+1<len(integer):
             if (integer[j]-integer[j-1])>=20 and (integer[j+1]-integer[j])>=20:
                  morethan20.append(integer[j])
    print("6) The numbers in the list which more than or less 20 from any other number in the list:",morethan20[0:])

        
    
#f001(list1, count)
#f002(list2, count)
#f03(list3)
#f004(list4)
#f005(coords,cordsection)
#f007(integer)