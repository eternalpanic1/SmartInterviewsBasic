'''
Given a matrix of size N x M, print column-wise sum, separated by a newline.

Input Format

The first line of input contains N, M - the size of the matrix. Its followed by N lines each containing M integers - elements of the matrix.

Constraints

1 <= N, M <= 100
-106 <= ar[i] <= 106

Output Format

Print column-wise sum of the matrix, separated by newline.
'''

n , m = map(int,input().split())
sum = [0 for k in range(m)]
for i in range(n):
    ar = [int(j) for j in input().split()]
    for k in range(m):
        sum[k] += ar[k] 
    
for i in sum:
    print(i)
    
