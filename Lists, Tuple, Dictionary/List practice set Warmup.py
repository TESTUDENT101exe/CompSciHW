list1=[[1,2,6],[6,1,2,3],[13,6,1,2,3]]
list2=[1,2,3]
list5=[[2, 1, 2, 3, 4],[2,2,0],[1,3,5]]
list4=[[2,5],[4, 3, 10, 5, 6],[4, 5, 10, 15, 16, 0, 4]]
newlist1=[]

def f001(list1):
    for i in range(len(list1)):
        if list1[i][0]==6 or list1[i][len(list1)-1]==6:
            print(True)
        else:
            print(False)

def f002(list2):
    list2.reverse()
    print(list2)

def f003(list1):
    newlist1=list1[2][0::(len(list1[2])-1)]
    print(newlist1)

def f004(list4):
    for i in range(len(list4)):
        for j in range(len(list4[i])):
            if list4[i][j]==2 or list4[i][j]==3:
                has23=True
        if has23==True:
            print(True)
            has23=False
        else:
            print(False)

def f005(list5):
    for i in range(len(list5)):
        evencount=0
        for j in range(len(list5[i])):
            if list5[i][j]%2==0:
                evencount+=1
        print(evencount)

#f001(list1)
#f002(list2)
#f003(list1)
#f004(list4)
#f005(list5)


