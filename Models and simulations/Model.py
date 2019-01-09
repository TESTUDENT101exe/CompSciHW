import matplotlib.pyplot as plt
import math
from random import randint as rand
population=1
starvation_rate_baseline = 0.01
predator_rate=0.1
step=12
birth_rate=0.15
death_rate=0.1
Holocaust=False
Spanish_INQUISITION=False
begin=False
x_coords = []
y_coords = []

for i in range(0, 100):
    if population>0:
        current_starvation_rate = starvation_rate_baseline * math.log(population,10)
    for j in range(0, population):
        if j<=100*birth_rate:
            population += int(rand(1,15))
    for l in range(0, population):
        if rand(0,100)<=100*death_rate:
            population -= 1
        if rand(0,100)<=100*predator_rate:
            population -= 1
        if l<=100*current_starvation_rate:
            population -= 1
    if rand(1,500)==1 and Holocaust!=True:
        population -= int(population*0.8)
        print("Hitler Did Nothing Wrong")
        Holocaust=True
    if rand(1,200)==1 and Spanish_INQUISITION!=True:
        population -= int(population*0.6)
        print("Nobody Expects The Spanish Inquisition")
        Spanish_INQUISITION=True
    x_coords.append(i * step)
    y_coords.append(population)

plt.figure()
plt.plot(x_coords, y_coords)
plt.xlabel("Hours")
plt.ylabel("Population")
plt.title('Tribble Population Growth')
plt.show()

