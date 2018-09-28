'''
print("Question 1) 2) 3)")
a=10
b=20
c=30
def foo1(a,b):
    a=b+c
    print(a)
    return(a)

def foo2(b,c):
    b=a+c
    print(b)
    return(b)

def foo3(a,c):
    c=a+b
    print(c)
    return(c)

def combine():
    print("Global Sum:",a+b+c)
    print("Local Sum:",foo1(a,b)+foo2(b,c)+foo3(a,c))
combine()
Rewrite Foo1
def foo1(a):
a=b+c
print(a)
'''
'''
print("4)")
#Triple Function
def add(num1,num2):
    return num1+num2
def triple(num):
    return add(num,add(num,num))
#Quad Function
def quadruple(num):
    return add(add(num,num),add(num,num))

print(quadruple(5))
'''
