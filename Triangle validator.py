'''
Given the length of 3 sides of a triangle, check whether the triangle is valid or not.

Input Format

First and only line of input contains three integers A, B, C - length of sides of the triangle.

Constraints

1 <= A, B, C <= 109

Output Format

Print "Yes" if you can construct a triangle with the given three sides, "No" otherwise.
'''

s1,s2,s3 = map(int,input().split())

if(s1+s2>s3 and s2+s3>s1 and s3+s1>s2):
    print("Yes")
else:
    print("No")
