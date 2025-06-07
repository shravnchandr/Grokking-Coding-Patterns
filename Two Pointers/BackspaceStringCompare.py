class Solution:
    def backspaceCompare(self, stringX: str, stringY: str) -> bool:
        listX, listY = list(), list()

        for char in stringX:
            if char == '#':
                if listX:
                    listX.pop()
            else:
                listX.append(char)

        for char in stringY:
            if char == '#':
                if listY:
                    listY.pop()
            else:
                listY.append(char)

        new_stringX, new_stringY = ''.join(listX), ''.join(listY)

        return new_stringX == new_stringY
    
