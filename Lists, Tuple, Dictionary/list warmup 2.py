numlist1=[2,6,5,3,46]
numlist2=[2,4,1,3,5,1]
low1=100000
low2=100000
alpha=[3,2,5,"adaw","adw",24]
digit=[5,8,3,2342,234,"adaw","adw",24,"eaewea"]

def smallest(numlist1,numlist2,low1,low2):
    for i in range(len(numlist1)-1):
        for j in range(len(numlist2)-1):
            if numlist1[i]==numlist2[j]:
                if numlist2[j]<low1:
                    low1=numlist2[j]
                elif numlist2[j]<low2:
                    low2=numlist2[j]
    print("1)",low1,",",low2)


def even(numlist1):
    for k in range(len(numlist1)-1):
        if numlist1[k]%2==1:
            del numlist1[k]
    print("2)",numlist1[0:])
    

def strint(alpha,digit):
    for l in range(len(alpha)-1):
        for m in range(len(digit)-1):
            if type(alpha[l])==int:
                digit.append(alpha[l])
            if type(digit[m])==str:
                alpha.append(digit[l])
    print("3)",alpha[0:],"\n",digit[0:])
smallest(numlist1,numlist2,low1,low2)
even(numlist1)
strint(alpha,digit)
