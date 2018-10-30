#Imported Files
import pygame
import random
import time



#Question 1 10x5 Grid
print("1) 10x5 Grid")
for i in range(0,5):
    for j in range(0,10):
        print("*", end=" ")
    print("\n")



#Question 2 Triangle
print("2) Triangle")
for i in range(0,6):
    for j in range(6-i):
        print(" ", end=" ")
    for j in range(1,i):
        print("*", end = " ")
    for i in range(i, 0, -1):
        print("*", end = " ")
    print("\n")


#Question 3 X in the square
print("3) x in Square")
distance1=0
B=int(input("Input base size:"))
H=int(input("Input Height:"))
def makeX(B,H):
    global distance1
    distance2=(B-1)
    for i in range(0,H):
        for j in range(0,B):
            if i==0 or i==H-1:
                print("*", end=" ")
            elif j==0 or j==B-1:
                print("*", end=" ")
            elif j==distance1:
                print("*", end=" ")
            elif j==distance2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("\n", end="")
        distance1=distance1+1
        distance2=distance2-1
makeX(B,H)


# 4) Pygame Checker Board
print("4) Pygame Checker Board")
screen = pygame.display.set_mode((500,500))
y=110
running =True
drawn=False
screen.fill((255,255,255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    while drawn==False:
        for i in range(0,5):
            if i==1 or i==3:
                x=180
                for g in range(0,2):
                    pygame.draw.rect(screen, (0, 0, 0), ((x, y), (50, 50)))
                    x+=100
            elif i==0 or i==2 or i==4:
                x=130
                for j in range(0,3):
                    pygame.draw.rect(screen, (0, 0, 0), ((x, y), (50, 50)))
                    x+=100
            y+=50
        drawn=True
    pygame.display.update()
pygame.quit()


# Question 5 Color Changing Pyrimid
print("5) Pygame Color Changing Pyrimid")
screen = pygame.display.set_mode((550 ,500))
r=0
g=0
b=0
color=[r ,g ,b]
y=80
running=True
drawn=False
screen.fill((255 ,255 ,255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if drawn==True:
        y=80
        for f in range(0 ,3):
            n=random.randint(0 ,255)
            color[f]=n
        time.sleep(1)
        drawn=False
    while drawn==False:
        for i in range(0 ,6):
            x=0
            for j in range(6-i):
                x+=50
            for j in range(1,i):
                pygame.draw.rect(screen, color[0:], ((x, y), (50, 50)))
                x+=50
            for i in range(i, 0, -1):
                pygame.draw.rect(screen, color[0:], ((x, y), (50, 50)))
                x+=50
            y+=50
        drawn=True
    pygame.display.update()
pygame.quit()
