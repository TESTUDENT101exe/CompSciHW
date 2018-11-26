import pickle
import operator
num_of_movies=0
Average_Time_per_Year={}
Num_of_x_movies2={}
Num_of_x_movies={}
Num_per_Year={}
Num_per_Director={}
Num_per_Actor={}
By_director={}
Dire_key=[]
By_year={}
Year_key=[]
By_actress={}
Actress_key=[]
By_actor={}
Actor_key=[]
Directors=[]

with open('movie.txt', 'r') as f:
    first_line=f.readline()
    MovieAttributes=first_line.strip().split(';')
    f.readline()
    MovieData=[]
    for line in f.readlines():
        Data=line.strip().split(';')
        MovieData.append(list(Data))

with open('movie2.txt', 'w') as f:
    for i in MovieAttributes:
        i = i.replace('\t', '')
        f.write(i + '\t')
    f.write('\n')
    for movie in MovieData:
        for item in movie:
            item = item.replace('\t', '')
            f.write(item + '\t')
        f.write('\n')

for i in range(len(MovieData)):

    for k in range(0,8):
        if MovieData[i][6]=='':
            MovieData[i][6] = "No Director"
        elif MovieData[i][1]=='':
            MovieData[i][1] = 0
        elif MovieData[i][k]=='':
            MovieData[i][k] = "No Data"

    MovieData[i][6]=MovieData[i][6].replace('\t', ' ')
    MovieData[i][4]=MovieData[i][4].replace('\t', ' ')
    MovieData[i][5]=MovieData[i][5].replace('\t', ' ')

    #Director
    if MovieData[i][6] not in By_director:
        By_director[MovieData[i][6]]=[]
        By_director[MovieData[i][6]].append(MovieData[i])
        Num_per_Director[MovieData[i][6]]=1
        Dire_key.append(MovieData[i][6])
    else: 
        Num_per_Director[MovieData[i][6]]+=1
        By_director[MovieData[i][6]].append(MovieData[i])

    #Actor
    if MovieData[i][4] not in By_actor:
        By_actor[MovieData[i][4]]=[]
        By_actor[MovieData[i][4]].append(MovieData[i])
        Num_per_Actor[MovieData[i][4]]=1
        Actor_key.append(MovieData[i][4])
    else: 
        Num_per_Actor[MovieData[i][4]]+=1
        By_actor[MovieData[i][4]].append(MovieData[i])

    #Actress
    if MovieData[i][5] in By_actress:
        By_actress[MovieData[i][5]].append(MovieData[i])
        
    else: 
        By_actress[MovieData[i][5]]=[]
        By_actress[MovieData[i][5]].append(MovieData[i])
        Actress_key.append(MovieData[i][5])

    #Year
    if MovieData[i][0] in By_year:
        By_year[MovieData[i][0]].append(MovieData[i])
        Num_per_Year[MovieData[i][0]]+=1
    else: 
        By_year[MovieData[i][0]]=[]
        Num_per_Year[MovieData[i][0]]=1
        By_year[MovieData[i][0]].append(MovieData[i])
        Year_key.append(MovieData[i][0])
Year_key.sort()

#average Length of movies per year
def average_year():
    for i in range(0,len(Year_key)):
        total=0
        for j in range(0,len(By_year[Year_key[i]])):
            total+=int(By_year[Year_key[i]][j][1])
        total=round(total/len(By_year[Year_key[i]]),2)
        Average_Time_per_Year[Year_key[i]]=total
    for k in range(0,len(Year_key)):
        print(Year_key[k],':',Average_Time_per_Year[Year_key[k]],'Minutes')
    #Pickle Data For Average Year
    with open('AverageYear.pickle', 'wb') as f:
        pickle.dump(Average_Time_per_Year, f)
    with open('YearLabel.pickle', 'wb') as g:
        pickle.dump(Year_key, g)

#Movies per Year
def per_year():
    MoviePerYear=[]
    for j in range(0,len(Year_key)):
        print(Year_key[j],':',Num_per_Year[Year_key[j]])
        MoviePerYear.append(Num_per_Year[Year_key[j]])
    #Pickle Data For Average Year
    with open('MoviePerYear.pickle', 'wb') as f:
        pickle.dump(MoviePerYear, f)

#Number of Directors who have produced x movies
def Per_Director(num_of_movies):
    x=0
    for j in range(0,100):
        num_of_movies+=1
        x+=1
        Num_of_x_movies[x]=0
        for k in range(0,len(Dire_key)):
            if Num_per_Director[Dire_key[k]]==num_of_movies:
                Num_of_x_movies[x]+=1
    for i in range(1,x):
        if Num_of_x_movies[i]!=0:
            print(Num_of_x_movies[i],'directors made:',i,'movies')
            Directors.append(Num_of_x_movies[i])
    with open('Num_of_x_movies.pickle', 'wb') as g:
        pickle.dump(Num_of_x_movies, g)

#Number of Actors who have produced x movies
def Per_actor():
    x=0
    num_of_movies2=0
    for j in range(0,100):
        num_of_movies2+=1
        x+=1
        Num_of_x_movies2[x]=0
        for k in range(0,len(Actor_key)):
            if Num_per_Actor[Actor_key[k]]==num_of_movies2:
                Num_of_x_movies2[x]+=1
    for i in range(1,x):
        if Num_of_x_movies2[i]!=0:
            print(Num_of_x_movies2[i],'actors acted in:',i,'movies')


#average_year()
per_year()
#Per_Director(num_of_movies)
#Per_actor()
#print(len(Dire_key))
#print(Directors[0:])