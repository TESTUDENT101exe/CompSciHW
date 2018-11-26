import pickle
import matplotlib.pyplot as plt

Directors = []
labels=[]

with open('Num_of_x_movies.pickle', 'rb') as f:
    Num_of_x_movies = pickle.load(f)

for i in range(1,100):
   if Num_of_x_movies[i]!=0:
     labels.append(i)
     Directors.append(Num_of_x_movies[i])


fig, ax = plt.subplots()
bar_width = 0.5

bar1_index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
label_tick = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

rects1 = ax.bar(bar1_index, Directors, bar_width, color='b')

ax.set_xlabel('Number Of Movies Produced')
ax.set_ylabel('Number Of Directors')
ax.set_title('Number of Directors Who Have Produced \'x\' Number Of Movies')
ax.set_xticks(label_tick)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()
plt.show()

