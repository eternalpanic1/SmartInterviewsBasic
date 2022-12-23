'''
For a given positive integer - N, compute Nth fibonacci number.

Input Format

First and only line of input contains a positive number - N.

Constraints

1 <= N <= 20

Output Format

Print the Nth fibonacci number.
'''

num = int(input())

fib0 = 0
fib1 = 1
out = 1
for i in range (0,num-1):
    out = fib0 + fib1
    fib0 = fib1
    fib1 = out
print(out)
