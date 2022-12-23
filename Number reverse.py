'''
Given a number N, reverse the number.

Input Format

First and only line of input contains a integer - N.

Constraints

-1018 <= N <= 1018

Output Format

Print the reversed number.

Sample Input 0

1344
Sample Output 0

4431
'''


num = int(input())
rev = 0
if(num<0):
    print("-",end="")
num = abs(num)
while num != 0:
    digit = num % 10
    rev = (rev * 10) + digit
    num //= 10
print(rev)
