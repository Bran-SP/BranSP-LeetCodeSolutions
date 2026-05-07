class Solution:#given an input string s and pattern p, implement regex matching with support for '.' and '*' according to specifications given in LeetCode Problem 10
    def isMatch(self, s: str, p: str) -> bool:
        def cleanAsts(as: str, ind: int) -> int:
            while as[ind] == '*':#get rid of any repeating *s at the start of each loop
                        ind += 1
            return ind
        if s == p: return True #easiest case
        elif len(p) == 0: return False #if pattern str is empty
        elif len(s) == 0:
            for ps in p:
                if ps != '*': return False 
            return True #s=0 allowed if p is *s only
        elif '*' not in p and '.' not in p: return False #if not using regex at this point
        else:
            j = 0
            wait = 0
            for i, c in enumerate(s):
                if j < len(p) and p[j] == '*' and (j == 0 or p[j - 1] == '*'):
                    j = cleanAsts(p, j)
                if j < len(p) and wait == 0:
                    if p[j] == '.' or p[j] == c:
                        j += 1
                    elif p[j] != '*':
                        if j + 1 >= len(p) or p[j + 1] != '*':
                            return False
                        else:
                            j += 2
                    else:#if it is *
                        if p[j - 1] == c:
                            continue
                        elif p[j - 1] == '.':
                            #nightmare case
                            if j == len(p) - 1:
                                return True
                            else:
                                j += 1
                                while p[j] == '*':
                                    if j == len(p) - 1:
                                        return True
                                    j += 1
                                if p[j] in s[i:len(s)]:
                                    wait = s.index(p[j]) - i
                                else: 
                                    return False
                        else:
                            j = cleanAsts(p, j)
                elif wait:
                    wait -= 1
                else:
                    return False #if we reach end of p before end of s, failed
                        
            return True #if we get through all of s without fail, success!