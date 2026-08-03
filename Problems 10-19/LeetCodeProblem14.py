class Solution: #Given array of strs, return longest common prefix amongst them
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        choice = min(x for x in strs) #pick the min sized str so we never go out of bounds later

        for i, c in enumerate(choice):#important to go char by char before going str by str to save small time
            for j, s in enumerate(strs):
                if s[i] != c:
                    return ans
            ans += c

	return ans