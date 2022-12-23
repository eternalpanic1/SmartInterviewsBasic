'''
Print right-angled triangle pattern using integers. See example for more details.

Input Format

First line of input contains a single integer N - the size of the triangle.

Constraints

1 <= N <= 50

Output Format

For the given integer, print the right-angled triangle pattern.
Sample Input 0

6
Sample Output 0

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
'''


num = int(input())
temp = 1

for i in range (1,num+1):
    for j in range (i):
        print(temp, end=" ")
        temp += 1
    print("")
    
    
