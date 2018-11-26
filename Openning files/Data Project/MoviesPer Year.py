import pickle
import matplotlib.pyplot as plt

Index=[]
X_axis_label=[]

with open('MoviePerYear.pickle', 'rb') as f:
    MoviePerYear = pickle.load(f)
with open('YearLabel.pickle', 'rb') as g:
    Year_key = pickle.load(g)

for i in range(0, len(Year_key)):
   Index.append(i)
   if int(Year_key[i]) % 10==0:
        X_axis_label.append(Year_key[i])
   else:
        X_axis_label.append(' ')

fig,ax = plt.subplots()
ax.set_xlabel('Year')
ax.set_ylabel('Number Of Movies')
ax.set_title('Number of Movies Produced Per Year')
ax.set_xticks(Index)
ax.set_xticklabels(X_axis_label)

plt.plot(MoviePerYear, '-b')
fig.tight_layout()
plt.show()
