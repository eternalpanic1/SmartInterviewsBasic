'''
Given a string, print count of vowels and consonants in the string.

Input Format

Input contains a string S, consisting of lowercase and uppercase characters.

Constraints

1 <= len(S) <= 100

Output Format

Print count of vowels and consonants in the given string, separated by space.

Sample Input 0

aBxbbiAasPw
Sample Output 0

4 7
'''

vowels = 0;  
consonants = 0;

instr = input().lower()
for i in range(0,len(instr)):
    if(instr[i] in ("a","e","i","o","u")):  
        vowels += 1;  
    else:
        consonants += 1;

print(vowels, consonants)
