'''
Given a positive integer - N, print the number of multiples of 3, 5 between [1, N].

Input Format

First and only line of input contains a positive integer - N.

Constraints

1 <= N <=1018

Output Format

Print the number of multiples of 3, 5 in range of 1 to N.

Sample Input 0

12
Sample Output 0

6
'''

num = int(input())
print((num//3) + (num//5) - (num//15))
