class Solution:#Given n pairs of parentheses, generate all combinations of well-formed parentheses
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def recurse(openP, closeP):
            if openP == closeP == n:#If we use all our parentheses, we've completed a list entry
                ans.append("".join(stack))
                return
            if openP < n:#This case represents the choice of using the open parentheses
                stack.append("(")
                recurse(openP + 1, closeP)
                stack.pop()
            if closeP < openP:#This case represents the choice of using the closed parentheses
                stack.append(")")
                recurse(openP, closeP + 1)
                stack.pop()

	#By popping after every recursive call, we basically ensure that we have the code check every critical juncture where a parentheses could be used
        recurse(0, 0)
        return ans
