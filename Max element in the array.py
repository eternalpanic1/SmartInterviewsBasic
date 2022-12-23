'''
Find maximum element from the given array of integers.

Input Format

First line of input contains N - the size of the array and second line contains the elements of the array.

Constraints

1 <= N <= 100
-109 <= ar[i] <= 109

Output Format

Print the maximum element of the given array.

Sample Input 0

5
-2 -19 8 15 4
Sample Output 0

15
'''

size = int(input())
my_array = [int(i) for i in input().split()]


max = my_array[0]
for i in range(1, size):         
     if my_array[i] > max:
            max = my_array[i]  

print(max)
