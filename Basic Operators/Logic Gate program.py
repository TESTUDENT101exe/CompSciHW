a=(0,0,0,0,1,1,1,1)
b=(0,0,1,1,0,0,1,1)
c=(0,1,0,1,0,1,0,1)
x=0
final=[]

for i in range(0,8):
    if (a[i] and b[i])==1 or (a[i] and c[i])!=1:
        x=1
    else:
        x=0
    final.append(x)

print(final[0:])
