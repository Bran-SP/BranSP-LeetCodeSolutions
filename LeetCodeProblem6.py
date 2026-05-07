class Solution:#Make input string s display in a zigzag pattern for a given number of rows
    def convert(self, s: str, numRows: int) -> str:
        arr = [""] * numRows
        modDir = 1 #this will be 1 or -1 to pick the direction rNum goes in
        rNum = 0 #variable to store what row of the list we should put a character in

        if numRows == 1:
            return s
        for i, c in enumerate(s):
            if i != 0 and i % (numRows - 1) == 0:
                modDir *= -1 #If you reach the end of a zigzag, flip
            arr[((rNum + 1) % (numRows)) - 1] += c #Place each character in the right row
            rNum += modDir #update row
        
        return "".join(arr) #flattens it down into one array and returns it