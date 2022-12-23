'''
Given two integers a and b, compute a power b.
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format

First and only line of input contains two positive integers a and b.

Constraints

1 <= a <= 100
0 <= b <= 9

Output Format

Print a power b.
'''


arr = [int(i) for i in input().split()]
print(arr[0] ** arr[1])
