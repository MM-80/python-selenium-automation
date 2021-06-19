# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

number = int(input('Enter an integer number'))
remainder = number % 2
if remainder == 0:
    print(number, 'is an even Number')
else:
    print(number, 'is an odd Number')