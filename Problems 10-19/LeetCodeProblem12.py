class Solution:#Given an int, convert to roman numerals (only can be as big as 3999)
    def intToRoman(self, num: int) -> str:
        converTable = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        #Table above makes it so that we dont need a bunch of different cases
        ans = ""

	#Just go backwards through table and place characters when appropriate.
        for i, (rome, val) in enumerate(reversed(converTable)):
            ans += rome * (num // val)
            num %= val
        
        return ans