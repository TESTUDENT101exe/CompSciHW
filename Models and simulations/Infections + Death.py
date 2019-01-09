import matplotlib.pyplot as plt
import math
from random import randint as rand
population=100
Susceptible=0.90
Infected=0.10
Recovered=0.00
Dead=0.00
Gamma=0.06
Beta=0.1
Alpha=0.04
steps=100
graph_susceptible = []
graph_infected = []
graph_recovered = []
graph_dead = []
Days=[]

for i in range(0, steps):
    new_infected = Beta * Infected * Susceptible
    new_recovered = Gamma * Infected
    Death = Alpha * Infected

    Susceptible-= new_infected + Death
    Infected+= (new_infected-new_recovered)
    Recovered +=new_recovered
    Dead+=Death
    Days.append(i)
    graph_infected.append(Infected)
    graph_recovered.append(Recovered)
    graph_susceptible.append(Susceptible)
    graph_dead.append(Dead)
    print(graph_infected[0:])

plt.figure()
plt.plot(Days, graph_infected, label='Infected')
plt.plot(Days, graph_dead, label='Dead')
plt.plot(Days, graph_recovered, label='Recovered')
plt.plot(Days, graph_susceptible, label='Susceptible')
plt.legend(loc='upper right')
plt.xlabel("Days")
plt.ylabel("Amount Of Population")
plt.title('Infectious Disease')
plt.show()

print("Total:", int(Recovered+Dead+Infected+Susceptible))
