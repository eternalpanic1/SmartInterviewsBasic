'''
Print sum of all odd elements in an array.

Input Format

First line of input contains N - the size of the array and second line contains array elements.

Constraints

1 <= N <= 100
-109 <= ar[i] <= 109

Output Format

Print sum of all odd elements of the given array.
'''
n = int(input())
arr = [int(i) for i in input().split()]

oddsum = 0
for i in range(0,n):
    if(arr[i] % 2 != 0):
        oddsum += arr[i]

print(oddsum)

