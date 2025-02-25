# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        hashOfS = [[] for x in range(numRows)]

        goBack = False
        index = 0
        for x in s:
            hashOfS[index].append(x)
            if index < numRows-1 and goBack == False:
                index += 1
                continue
            if index == 0 and goBack == True:
                index += 1
                goBack = False
                continue
            index -= 1
            goBack = True
        s = ""
        for rows in hashOfS:
            s += "".join(rows)
                  

        return s
