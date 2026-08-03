class Solution:#Given Roman Numeral, convert to int (max is 3999)
    def romanToInt(self, s: str) -> int:
        ans = 0
        romeDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
	#Table above that only includes different one character numerals

        for i, c in enumerate(s):
            if c in "CXI" and i < len(s) - 1 and romeDict[c] < romeDict[s[i + 1]]:
                ans -= romeDict[c]#If char is a char that can indicate 4 or 9, subtract the value to make everything work
            else:
                ans += romeDict[c]#Otherwise just add value
        
        return ans