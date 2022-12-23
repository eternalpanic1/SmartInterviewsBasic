'''
Given a matrix of size N x M, print whether it is a sparse matrix or not.
Note: If a matrix contain 0 in more than half of its cells, then it is called a sparse matrix.

Input Format

First line of input contains N, M - size of the matrix. Its followed by N lines each containing M intergers - elements of the matrix.

Constraints

1 <= N, M <= 100
0 <= ar[i] <= 109

Output Format

Print "Yes" if the given matrix is a sparse matrix, otherwise print "No".

Sample Input 0

2 3
5 0 0
0 8 0
Sample Output 0

Yes
'''

n,m = map(int,input().split())
arr = [0 for i in range(n)]

for i in range(n):
    arr[i] = [int(j) for j in input().split()]

ct = 0
for i in arr:
    for j in i:
        if (j == 0):
            ct += 1

if(ct > (n*m)//2):
    print("Yes")
else:
    print("No")
