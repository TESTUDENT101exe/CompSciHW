# open('TXT file', 'r'="read")
# .strip()=Removes part at the end of the string
# .split()=split when a certain Character appears

#V1
'''f=open('Something.txt', 'r')
lines=[]
for line in f.readlines():
    print(line.strip())
    line=line.strip().split()
    line=tuple(line)
    lines.append(line)
f.close()

print(lines[0:])
'''

import codecs

#V2
lines=[]
with open('Something.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())
        line=line.strip().split()
        line=tuple(line)
        lines.append(line)
print(lines[0:])
