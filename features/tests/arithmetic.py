"""
Below The Arithmetical Mean
When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
The arithmetical mean is the sum of all elements divided by the number of elements.
Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

"""
print("Calculate the Average of N numbers ")
n = int(input("How many numbers ?"))
nums = []
sum = 0
for i in range(n):
    a = int(input("Enter a number"))
    nums.append(a)
    sum += nums[i]

    avg = sum/n
    print("Average of numbers is ", avg)

"""
Two Lowest Elements
When given a list of elements, find the two lowest elements.
They can be equal to each other or different.
Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

"""

mylist = [198, 3, 4, 9, 10, 9, 2]
mylist.sort()
print(mylist)

print("First lowest element is:",mylist[0])
print("Second lowest element is:",mylist[1])


