# Q#1
# Compute the sum of digits in all numbers from 1 to n. When a user enters
# a number n, find the sum of digits in all numbers from 1 to n.

n = int(input('Enter a number:'))
total = 0
while n > 0:
    digit = n % 10
    total = total+digit
    n = n//10
print("The total sum of digits is:", total)

