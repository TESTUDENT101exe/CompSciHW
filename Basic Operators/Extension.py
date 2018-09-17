num=input("Input a integer number")
while num.isdigit()==False:
    try:
        int(num)
    except ValueError:
        num=input("Input a integer number")
if num % 2 == 0 and num != 0:
    print('The inputed number is Even')
else:
    print('The inputed number is Odd')

print('---------------------------------------')

binary=bin(num)
