class Solution:#Convert a string to a 32bit integer using the algorithm defined in LeetCode Problem 8
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() #ignore leading whitespace
        sign = 1

	#determine the sign of the int
        if len(s) == 0:
            return 0
        elif s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        elif not s[0].isnumeric():
            return 0
        
        ans = ""
        for c in s:
            if not c.isnumeric():
                break
            elif ans == "" and c == '0':#skip leading 0s
                continue
            else:#read in each digit that isnt leading 0s
                ans = "".join([ans, c])

        if ans == "":
            return 0

        ans = int(ans)
	#deal with rounding
        if ans.bit_length() >= 32:
            if sign == 1:
                return 2147483647
            else:
                return -2147483648
        else:
            return sign * ans
