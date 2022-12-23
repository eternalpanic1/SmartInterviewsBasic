'''
Given a non-negative integer - N, print the sum of digits of the given number.

Input Format

First and only line of input contains a non-negative integer N.

Constraints

0 <= length(N) <= 103

Output Format

Print the sum of digits of the given number.
'''

num = int(input())
sum = 0
while (num > 0):
    sum = sum + num % 10
    num = num // 10
    
print(sum)
