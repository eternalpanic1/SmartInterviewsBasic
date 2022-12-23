'''
Find a duplicate element in the given array of integers. There will be only a single duplicate element in the array.
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format

First line of input contains size of the array - N and second line contains the elements of the array.

Constraints

2 <= N <= 100
0 <= ar[i] <= 109

Output Format

Print the duplicate element from the given array.
'''

n = int(input())
arr = [int(i) for i in input().split()]

for i in range(0,n):
    if(arr.count(arr[i]) > 1):
        print(arr[i])
        break
