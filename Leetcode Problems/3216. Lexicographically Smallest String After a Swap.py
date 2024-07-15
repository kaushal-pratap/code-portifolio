'''3216. Lexicographically Smallest String After a Swap

https://leetcode.com/contest/weekly-contest-406/problems/lexicographically-smallest-string-after-a-swap/description/
'''

class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)
        result = ''
        for i in range(len(s)-1):
            j = i + 1
            if int(s[i]) % 2 == 0 and int(s[j]) % 2 == 0:
                if int(s[i]) > int(s[j]):
                    s[i],s[j] = s[j],s[i]
                    break
            elif int(s[i]) % 2 != 0 and int(s[j]) % 2 != 0:
                if int(s[i]) > int(s[j]):
                    s[i],s[j] = s[j],s[i] 
                    break
            else:
                continue
        for j in s:
            result += j
        return result