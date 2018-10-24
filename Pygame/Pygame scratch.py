import time
import random
x=300
y=300
end=False
while end!=True:
    time.sleep(4)
    steps=random.randint(10,50)
    direction=random.randint(1,4)
    if direction==1:
        x+=steps
    elif direction==2:
        y+=steps
    elif direction==3:
        x=x-steps
    elif direction==4:
        y=y-steps
    if x>=600 or x<=0 or y>=600 or y<=0:
        end=True
    print(x,y)
