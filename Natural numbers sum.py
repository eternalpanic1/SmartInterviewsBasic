'''
Given a positive integer N, print the sum of 1st N natural numbers.

Input Format

First and only line of input contains a positive integer - N.

Constraints

1 <= N <= 104

Output Format

Print the sum of 1st N natural numbers.
'''


n = int(input())

print(int(n * (n+1)/2))
