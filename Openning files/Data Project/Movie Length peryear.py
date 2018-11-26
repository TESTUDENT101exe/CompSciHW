import pickle
import matplotlib.pyplot as plt

Index=[]
Time=[]
X_axis_label=[]

with open('AverageYear.pickle', 'rb') as f:
    Average_Time_per_Year = pickle.load(f)
with open('YearLabel.pickle', 'rb') as g:
    Year_key = pickle.load(g)

for k in range(0,len(Year_key)):
   Time.append(Average_Time_per_Year[Year_key[k]])
   Index.append(k)
   if int(Year_key[k]) % 10==0:
        X_axis_label.append(Year_key[k])
   else:
        X_axis_label.append(' ')

fig, ax = plt.subplots()
bar_width = 0.5

rects1 = ax.bar(Index, Time, bar_width, color='b')

ax.set_xlabel('Year')
ax.set_ylabel('Length Of Movie In Minutes')
ax.set_title('Average Length Of Movies Per Year')
ax.set_xticks(Index)
ax.set_xticklabels(X_axis_label)

fig.tight_layout()
plt.show()
