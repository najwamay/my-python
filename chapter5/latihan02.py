"""
Using loop, write a python code to print all integers between a to b which are multiples of 3

Note: 
a and b are inputs

Example:
Enter a : 3
Enter b : 20

output:
3, 6, 9, 12, 15, 18
"""

a = int(input("Enter a : "))
b = int(input("Enter b: "))

for i in range(a, b + 1):
    if i % 3 == 0:
        print(i)