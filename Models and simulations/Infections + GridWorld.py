from gridworld import GridWorld
from random import randint

setup=False
done=False
SIRD = [(0,255,0),(0,0,255),(255,255,255),(255,0,0)]
sim = GridWorld(60, 40, 10)
Death=0.5
RecoveryRate=0.7
time=3
stop=False

def sweep(cell, InfectionPercent):
    s = sim.get_surroundings(cell[0], cell[1], 3)
    for i in range(0, len(s)):
        for j in range(0, len(s[i])):
            if i == 0 or i==len(s)-1 or j==0 or j==len(s[i])-1:
                if s[i][j]==SIRD[1]:
                    InfectionPercent+=2
            elif i == 1 or i==len(s)-2 or j==1 or j==len(s[i])-2:
                if s[i][j]==SIRD[1]:
                    InfectionPercent+=5
            elif i == 2 or i==len(s)-3 or j==2 or j==len(s[i])-3:
                if s[i][j]==SIRD[1]:
                    InfectionPercent+=25
    return InfectionPercent

def Infected(cell, InfectionPercent):
    if randint(0,100)<=InfectionPercent:
        sim.set_cell(cell[0], cell[1], SIRD[1])

def DeathChance(cell, Death):
    if randint(0,1000)<=(Death*10):
        sim.set_cell(cell[0], cell[1], SIRD[3])
    else:
        return False

def Recovery(cell, RecoveryRate):
    if randint(0,1000)<=(RecoveryRate*10):
        sim.set_cell(cell[0], cell[1], SIRD[2])

while not done:
    done = sim.process_events()
    if setup==False:
        for i in range(0, 300):
            sim.set_cell(randint(0, 60), randint(0,40), SIRD[randint(0,1)])
        setup=True
    if time!=0:
        for cell in sim.cells:
            InfectionPercent=0
            color = sim.get_cell(cell[0], cell[1])
            if color==SIRD[0]:
                InfectionPercent=sweep(cell, InfectionPercent)
                print(InfectionPercent)
                Infected(cell, InfectionPercent)
        time-=1
    elif time==0 and stop==False:
        for cell in sim.cells:
            color = sim.get_cell(cell[0], cell[1])
            if color==SIRD[1]:
                Dead = DeathChance(cell, Death)
                if Dead==False:
                    Recovery(cell, RecoveryRate)
        stop=True

    sim.update()

sim.end()

