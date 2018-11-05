import random
diction={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

def f001(diction):
    for i in range(0,10000):
        num=str(random.randint(0,9))
        diction[num]+=1

    for j in range(0,10):
        print(j,":",diction[str(j)],end="\n")

def f002(diction):

f001(diction)