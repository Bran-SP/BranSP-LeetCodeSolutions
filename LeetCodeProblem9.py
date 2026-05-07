class Solution:#Given an integer x, return true if x is a palindrome, and false otherwise
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False #anything less than 0 wont be a palindrome

        div = 1
        while x >= 10 * div: 
            div *= 10 #set up div to be biggest digit in x

        while x: #turns out this syntax is the same as while x != 0 so it works here
            right = x % 10
            left = x // div

            if left != right: return False #if current ends dont match, not a palindrome
            
            #do the equivalent of moving pointers to next chars for palindrome string detection
            x = (x % div) // 10
            div = div // 100

        return True