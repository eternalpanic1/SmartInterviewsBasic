'''
Given an integer - N, print a string with the letter 'o' repeated for N times in the word Go...od.

Input Format

First and only line of input contains a single integer N.

Constraints

0 <= N<= 100

Output Format

Print the word Go..od with letter 'o' repeated N times.

Sample Input 0

4
Sample Output 0

Gooood
'''


times = int(input())

out = ['o' for i in range (0,times)]
out.append('d')
out.insert(0,'G')

for i in out:
    print(i, end="")
