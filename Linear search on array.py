'''
Given an array on integers, search a given key in the array using linear search.
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format

First line of input contains two integers, N - size of the array and K - search key. Second line contains the elements of the array.

Constraints

1 <= N <= 102
0 <= ar[i] <= 109

Output Format

If key is found, print the index of the array, otherwise print -1.

Sample Input 0

5 15
-2 -19 8 15 4
Sample Output 0

3
'''



def linear_search_recursive(index, target):
    if(index == -1):
        return -1
    if(array[index] == target):
        return index
    return linear_search_recursive(index-1, target)

arr = [int(i) for i in input().split()]
array = [int(i) for i in input().split()]
print(linear_search_recursive(arr[0]-1,arr[1]))
