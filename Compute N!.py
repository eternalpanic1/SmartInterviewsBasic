'''
Given a non-negative number - N, print N!

Input Format

First and only line of input contains a number - N.

Constraints

0 <= N <= 10

Output Format

Print factorial of N.
'''

n = int(input())
out = 1

for i in range (1,n+1):
    out = out*i
    
print(out)
