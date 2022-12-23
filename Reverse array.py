'''Print array in reverse order.
Note: Try solving this using recursion. Do not use any inbuilt functions/libraries for your main logic.

Input Format

First line of input contains N - the size of the array and second line contains the elements of the array.

Constraints

1 <= N <= 100
0 <= ar[i] <= 1018

Output Format

Print the given array in reverse order.'''


def reverse(point):
    if(point >= 0):
        print(arr[point] , end=" ")
        point = point - 1
        reverse(point)


n = int(input())
arr = [int(i) for i in input().split()]
reverse(n-1)
