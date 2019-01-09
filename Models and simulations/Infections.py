import matplotlib.pyplot as plt
import math
from random import randint as rand
population=100
Susceptible=0.90
Infected=0.10
Recovered=0.00
Gamma=0.01
Beta=0.05
steps=100
graph_susceptible = []
graph_infected = []
graph_recovered = []
Days=[]

for i in range(0, steps):
    new_infected = Beta * Infected * Susceptible
    new_recovered = Gamma * Infected

    Susceptible-= new_infected
    Infected+= (new_infected-new_recovered)
    Recovered +=new_recovered
    Days.append(i)
    graph_infected.append(Infected)
    graph_recovered.append(Recovered)
    graph_susceptible.append(Susceptible)
    print(graph_infected[0:])

plt.figure()
plt.plot(Days, graph_infected, label='Infected')
plt.plot(Days, graph_recovered, label='Recovered')
plt.plot(Days, graph_susceptible, label='Susceptible')
plt.legend(loc='upper right')
plt.xlabel("Days")
plt.ylabel("Amount Of Population")
plt.title('Infectious Disease')
plt.show()
