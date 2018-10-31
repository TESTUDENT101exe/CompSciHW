
#Import
import pygame
import random
import time

#Parts
steps=0
enddraw=False
running=True
failed=False
screen = pygame.display.set_mode((600 ,600))
screen.fill((255 ,255 ,255))
objxy=[300 ,300]
complete_obstruction=0

#Functions
def obj():
    pygame.draw.rect(screen, (0 , 0, 0), (objxy, (1 , 1)))
    
def move():
    global direct, failed, complete_obstruction
    runtime=0
    while runtime!=steps and failed!=True:
        if direct==1 and screen.get_at((objxy[0]+1, objxy[1])) != (0 ,0 ,0):
            objxy[0]+=1
        elif direct==2 and screen.get_at((objxy[0], objxy[1]+1)) != (0 ,0 ,0):
            objxy[1]+=1
        elif direct==3 and screen.get_at((objxy[0]-1, objxy[1])) != (0 ,0 ,0):
            objxy[0]=objxy[0]-1
        elif direct==4 and screen.get_at((objxy[0], objxy[1]-1)) != (0 ,0 ,0):
            objxy[1]=objxy[1]-1
        else:
            complete_obstruction+=1
            failed=True
        runtime+=1
        print(objxy[0:])
        obj()
        pygame.display.update()
        
def direction():
    global failed, direct, complete_obstruction
    if failed==False:
        complete_obstruction=0
        direct=random.randint(1 ,4)
    elif failed==True:
        if direct==4:
            direct=1
        else:
            direct+=1
        failed=False
        
#Basic Code
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#Main Code
    while enddraw!=True:
        direction()
        steps=random.randint(10 ,50)
        time.sleep(0.1)
        move()
        if complete_obstruction==5:
            enddraw=True
            print("Drawing Complete")
        elif objxy[0]<=0 or objxy[0]>=600 or objxy[1]<=0 or objxy[1]>=600:
            enddraw=True
            print("Drawing Complete")
pygame.quit()
