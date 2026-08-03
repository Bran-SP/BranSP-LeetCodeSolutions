class Solution:#Determine if an input string has parity between parentheses, brackets, and curly braces. Specifics defined in the problem statement of Leetcode 20
    def isValid(self, s: str) -> bool:
        stack = []

	#Stack solution. We know if a closed bracket is valid if we can pop its corresponding open bracket from the stack

        for i, c in enumerate(s):
            if c in "({[":
                stack.append(c)
            elif c == ")":
                if stack and stack.pop() == "(":
                    continue
                else:
                    return False
            elif c == "}":
                if stack and stack.pop() == "{":
                    continue
                else:
                    return False
            else:
                if stack and stack.pop() == "[":
                    continue
                else:
                    return False

	#If anything is left on the stack when we've read through the whole string, return False

        return False if stack else True