By_director={}
By_year={}
By_actress={}
By_actor={}
with open('movie.txt', 'r') as f:
    first_line=f.readline()
    MovieAttributes=first_line.strip().split(';')
    f.readline()
    MovieData=[]
    for line in f.readlines():
        Data=line.strip().split(';')
        MovieData.append(tuple(Data))

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

    if MovieData[i][6]=='':
        MovieData[i][6].replace('', "No Director")
    elif MovieData[i][4]=='':
        MovieData[i][4].replace('', "No Data")
    elif MovieData[i][5]=='':
        MovieData[i][5].replace('', "No Data")
    elif MovieData[i][0]=='':
        MovieData[i][0].replace('', "No Data")

    if MovieData[i][6] not in By_director:
        By_director[MovieData[i][6]]=[]
        By_director[MovieData[i][6]].append(MovieData[i])
    else: 
        By_director[MovieData[i][6]].append(MovieData[i])

    if MovieData[i][4] not in By_actor:
        By_actor[MovieData[i][4]]=[]
        By_actor[MovieData[i][4]].append(MovieData[i])
    else: 
        By_actor[MovieData[i][4]].append(MovieData[i])

    if MovieData[i][5] not in By_actress:
        By_actress[MovieData[i][5]]=[]
        By_actress[MovieData[i][5]].append(MovieData[i])
    else: 
        By_actress[MovieData[i][5]].append(MovieData[i])

    if MovieData[i][0] not in By_year:
        By_year[MovieData[i][0]]=[]
        By_year[MovieData[i][0]].append(MovieData[i])
    else: 
        By_year[MovieData[i][0]].append(MovieData[i])


for j in range(1,len(By_director)):
    print(MovieData[j][6] ,':', By_director[MovieData[j][6]],end='\n')