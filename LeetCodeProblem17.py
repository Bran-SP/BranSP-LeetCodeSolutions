class Solution:#Given a string containing digits from 2-9 inclusive, return all possible letter combos the number could represent (using the letters each number on an old phone would represent)
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"}#Here's a dict of the conversions. This is given in problem statement.

        ans = []

        def recurse(ind, currStr):
            if len(currStr) == len(digits):#If we have right number of letters, we've found one part of the solution list
                ans.append(currStr)
                return
            
            for i, c in enumerate(letter_map[digits[ind]]):#Call over and over to populate list with correct numbers of each letter
                recurse(ind + 1, currStr + c)
            return

        if digits:#If list isn't empty, call the recursive method
            recurse(0, "")

        return ans