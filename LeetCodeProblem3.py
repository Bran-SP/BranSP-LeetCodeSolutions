class Solution:#Given string s, return longest substring without duplicate characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        #First test some base cases to get them out of the way easily
        if not s:
            return 0
        if len(s) == 1:
            return 1
        #Idea is that we'll have a set of a substring we're looking at in order to
        #know if a duplicate appears.
        checkSet = set()
        ret = 1 #this will be the value we return, the "maximum length". We know the string
        # is at least 1 character long so we'll go ahead and put it at 1

        l = 0 #the left boundary of our "shifting window". We increment this if we see a
        # duplicate in order to only ever have to go through the whole string once

        for r, c in enumerate(s): #enum for fast runtime
            while c in checkSet: #if we find this character in our set, move window
                checkSet.remove(s[l])
                l += 1
            #otherwise, as the rightward barrier increments to include one more character, put
            #that character in the set to keep things rolling. Also update return value.
            checkSet.add(c)
            ret = max(ret, r - l + 1)
        return ret