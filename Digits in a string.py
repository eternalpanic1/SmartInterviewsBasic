'''
Given a string, check if it contains only digits.

Input Format

Input contains a string S, consisting of ascii characters.

Constraints

1 <= len(S) <= 100

Output Format

Print "Yes" if string contains only digits, "No" otherwise.

Sample Input 0

123456786543
Sample Output 0

Yes
Explanation 0

Self Explanatory

Sample Input 1

"Smart-Interviews"
Sample Output 1

No
'''


digits = ('1','2','3','4','5','6','7','8','9','0')

string = input()
count = 0
for i in string:
    if i not in digits:
        count += 1
        break
    else:
        pass

if(count>0): print("No")
else: print("Yes")
