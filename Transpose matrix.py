'''
Given a matrix of size N x M, print transpose of the matrix.

Input Format

First line of input contains N, M - the size of the matrix. Its followed by N lines each containing M integers - elements of the matrix.

Constraints

1 <= N, M <= 100
-109 <= ar[i] <= 109

Output Format

Print the transposed of the given matrix.

Sample Input 0

2 2
5 -1
19 8
Sample Output 0

5 19
-1 8
'''

n,m = map(int,input().split())
arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = [int(j) for j in input().split()]
    
    
for i in range(m):
    for j in range(n):
        print(arr[j][i],end=" ")
    print("")
