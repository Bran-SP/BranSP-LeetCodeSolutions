class Solution:#Given signed 32 bit int, x, return x with its digits reversed. If it would go outside the bounds of 32signed bit, return 0
    def reverse(self, x: int) -> int:
        #32 int max is 2,147,483,647
	#handle a base cases first
        if x < 10 and x > -10:
            return x
        elif x < 0:
            x *= -1
            rev = 0
            while x > 0:#go digit by digit, and if it threatens to go over, do a small check to know if it does or not
                if rev < 2147483640 or (rev == 2147483640 and x <= 8):
                    rev += x % 10
                    x = x // 10
                    if x > 0:
                        rev *= 10
                else:
                    return 0

            return -1 * rev
        else:
            rev = 0
            while x > 0:#same loop as in odd case
                if rev < 2147483640 or (rev == 2147483640 and x <= 7):
                    rev += x % 10
                    x = x // 10
                    if x > 0:
                        rev *= 10
                else:
                    return 0

            return rev