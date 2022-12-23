'''
Given the length and breadth of a rectangle, print area of the rectangle.

Input Format

First and only line of input contains two positive integers L - length of the rectangle and B - breadth of the rectangle.

Constraints

1 <= L, B <=109

Output Format

Print area of the given rectangle.
'''

l,b = map(int,input().split())
print(int(l) * int(b))
