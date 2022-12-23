'''
Given a matrix of size N x M, print row-wise sum, separated by a newline.
Note: Try to solve this without declaring/storing the matrix.

Input Format

First line of input contains N, M - the size of the matrix. Its followed by N lines each containing M integers - elements of the matrix.

Constraints

1 <= N, M <= 100
-106 <= ar[i] <= 106

Output Format

Print row-wise sum of the matrix, separated by a newline.
'''

n , m = map(int,input().split())
for i in range(n):
    sum = 0
    lst = [int(k) for k in input().split()]
    for j in lst:
        sum += j
    print(sum)
