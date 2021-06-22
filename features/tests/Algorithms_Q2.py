# Q#2
# Find max number from 3 values, entered manually from a keyboard.

a = int(input('Enter first integer'))
b = int(input('Enter second integer'))
c = int(input('Enter third integer'))
print('Maximo is ', end='')
if b <= a >= c:
    print(a)
elif a <= b >= c:
    print(b)
elif a <= b >= b:
    print(c)