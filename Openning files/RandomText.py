sentencelist=[]
sentence=''
with open('Random.txt', 'r') as f:
    for line in f.readlines():
        line=line.strip()
        sentence+=line

    for sent in sentence.split('.'):
        sentencelist.append(sent)

print(sentencelist[0:])
