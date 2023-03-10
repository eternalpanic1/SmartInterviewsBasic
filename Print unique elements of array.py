'''
Print unique elements of the array in the same order as they appear in the input.
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format

First line of input contains a single integer N - the size of array and second line contains array elements.

Constraints

1 <= N <= 100
0 <= ar[i] <= 109

Output Format

Print unique elements of the array.

Sample Input 0

7
5 4 10 9 21 4 10
Sample Output 0

5 9 21
'''


size = int(input())
arr = [int(i) for i in input().split()]

unique=[]
dupes=[]
for i in range(size):
    if(arr[i] in arr[i+1:]):
        dupes.append(arr[i])
    elif(arr[i] not in dupes):
        unique.append(arr[i])
            

for i in unique:
    print(i,end=" ")
