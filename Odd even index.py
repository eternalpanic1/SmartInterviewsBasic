'''
Given a string, print all the letters present at odd index, followed by the letters present at even index.

Input Format

Input contains a string S, consisting of ascii characters.

Constraints

1 <= len(S) <= 100

Output Format

Print letters present at odd index, followed by the letters present at even index.

Sample Input 0

afdg5tg
Sample Output 0

fgtad5g
'''


instr = input()
size = len(instr)
for i in range(1,size,2):
    print(instr[i],end="")
for i in range(0,size,2):
    print(instr[i],end="")
