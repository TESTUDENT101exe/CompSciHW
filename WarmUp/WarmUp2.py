Int=21
Float=3.14
STR="FALSE"
Bool=True
print('---------------------------------')
print(type(Int),type(Float),type(STR),type(Bool))
print('---------------------------------')
print(bool(Int),bool(Float),bool(STR),bool(Bool))
print('---------------------------------')
print(int(Float)+int(Bool))
print('---------------------------------')
print('Hex:',hex(Int),'\nBinary',bin(Int))
print('---------------------------------')
#The chr() method returns a character (a string) from an integer (represents unicode code point of the character).
print(chr(75))
#The ord() method returns a number (a integer) from an character (represents unicode point of the chracter)
print(ord('K'))
print('---------------------------------')
