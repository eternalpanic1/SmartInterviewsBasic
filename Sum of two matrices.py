'''
Given two matrices A and B each of size N x M, print sum of the matrices (A + B)..
Note: Try solving it by declaring only a single matrix.

Input Format

First line of input contains N, M - size of the matrices. Its followed by 2*N lines, each containing M integers - elements of the matrices. First N lines for matrix A and the next N lines for matrix B.

Constraints

1 <= N, M <= 100
-109 <= ar[i] <= 109

Output Format

Print sum of the 2 given matrices (A + B).

Sample Input 0

2 3
5 -1 3
19 8 4
4 5 -6
1 -2 12
Sample Output 0

9 4 -3
20 6 16
'''


n,m = map(int,input().split())
sum = [[0 for i in range(m)] for j in range(n)]

for l in range(2):
    for i in range(n):
        ar = [int(j) for j in input().split()]
        for k in range(m):
            sum[i][k] += ar[k] 

for i in range(n):
    for j in range(m):
        print(sum[i][j],end=" ")
    print("")
