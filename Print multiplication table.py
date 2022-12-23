'''
Print multiplication table for given integer N.

Input Format

First and only line of input contains a single integer N.

Constraints

-105 <= N <= 105

Output Format

Print multiplication table for given integer N.

Sample Input 0

9
Sample Output 0

9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90
'''

num = int(input())

for i in range(1,11):
    print(num,"*", i, "=", num*i)
