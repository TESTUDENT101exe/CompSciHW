def sum(V1,V2):
    print(V1+V2)
    return None
V1=input("Enter first number:")
V2=input("Enter second number:")
ans= sum(V1,V2)
print(ans)
print('--------------------------------------')
def combine(fs,ss):
    return (fs+ss)*repeat
fs=input("Enter first string:")
ss=input("Enter second string:")
repeat=int(input("Enter number of times the strings are printed:"))
Combined=combine(fs,ss)
print(Combined)
print('--------------------------------------')
vowels=0
def vowel_count1(word,vowels):
    for i in range (0,len(word)):
        if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u":
            vowels+=1
    print(vowels)
word=input("Type in a string value")
vowel_count1(word,vowels)
