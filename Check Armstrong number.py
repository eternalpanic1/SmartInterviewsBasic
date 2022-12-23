'''
Given an integer N, check whether it's an Armstrong number or not.
Note: Armstrong number is a number that is equal to the sum of cubes of its digits.

Input Format

First and only line of input contains a integer - N.

Constraints

0 <= N <= 109

Output Format

Print "Yes" if the number is an Armstrong number, "No" otherwise.
'''

num = int(input())
power = len(str(num))
temp = num
arm = 0
while(temp > 0):
    rem = temp % 10
    arm += (rem ** power)
    temp = temp//10

if(arm == num):
    print("Yes")
else:
    print("No")
