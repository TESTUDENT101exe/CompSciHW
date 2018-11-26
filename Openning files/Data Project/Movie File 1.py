import operator
num_of_movies=1
By_director={}
Dire_key=[]
By_year={}
Year_key=[]
By_actress={}
Actress_key=[]
By_actor={}
Actor_key=[]

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
        elif MovieData[i][k]=='':
            MovieData[i][k] = "No Data"

    #Director
    if MovieData[i][6] not in By_director:
        MovieData[i][6]=MovieData[i][6].replace('\t', ' ')
        By_director[MovieData[i][6]]=[]
        By_director[MovieData[i][6]].append(MovieData[i])
        Dire_key.append(MovieData[i][6])
    else: 
        By_director[MovieData[i][6]].append(MovieData[i])

    #Actor
    if MovieData[i][4] not in By_actor:
        MovieData[i][4]=MovieData[i][4].replace('\t', ' ')
        By_actor[MovieData[i][4]]=[]
        By_actor[MovieData[i][4]].append(MovieData[i])
        Actor_key.append(MovieData[i][4])
    else: 
        By_actor[MovieData[i][4]].append(MovieData[i])

    #Actress
    if MovieData[i][5] not in By_actress:
        MovieData[i][5]=MovieData[i][5].replace('\t', ' ')
        By_actress[MovieData[i][5]]=[]
        By_actress[MovieData[i][5]].append(MovieData[i])
        Actress_key.append(MovieData[i][5])
    else: 
        By_actress[MovieData[i][5]].append(MovieData[i])

    #Year
    if MovieData[i][0] in By_year:
        By_year[MovieData[i][0]].append(MovieData[i])
    else: 
        By_year[MovieData[i][0]]=[]
        By_year[MovieData[i][0]].append(MovieData[i])
        Year_key.append(MovieData[i][0])
Year_key.sort()

print(MovieData)