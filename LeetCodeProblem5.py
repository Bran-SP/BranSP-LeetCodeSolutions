class Solution:#Given string s, return longest palindromic substring in s
    def longestPalindrome(self, s: str) -> str:
        ret = ""
        retLen = 0

        for i in range(len(s)):
            offset = 0

            #even case
            while offset <= i and i + offset <= len(s) - 2 and s[i - offset] == s[i + 1 + offset]:
                if retLen < 2 or (2 * offset + 2) > retLen:
                    ret = s[(i - offset):(i + 2 + offset)]
                    retLen = 2 * offset + 2
                offset = offset + 1

            offset = 0 #gotta remember to reset offset before we go into a different case

            #odd case
            while offset <= i and i + offset <= len(s) - 1 and s[i - offset] == s[i + offset]:
                if (2 * offset + 1) > retLen:
                    ret = s[(i - offset):(i + 1 + offset)]
                    retLen = 2 * offset + 1
                offset = offset + 1
        
        return ret