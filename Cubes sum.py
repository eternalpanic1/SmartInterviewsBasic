'''
Given a positive integer N, print the sum of cubes of 1st N natural numbers.

Input Format

First and only line of input contains a positive integer - N.

Constraints

1 <= N <= 102

Output Format

Print the sum of cubes of 1st N natural numbers.
'''


num = int(input())

arr = [int(i**3) for i in range(0,num+1)]

out = 0
for i in arr:
    out += i
    
print(out)
