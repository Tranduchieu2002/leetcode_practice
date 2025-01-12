class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2:
            return False
        
        i = 0
        countCloseBracket, countOpenBracket = 0, 0
        for i in range(n):
            if s[i] == '(' and locked[i] == '1':
                countOpenBracket += 1
                countCloseBracket += 1
            elif s[i] == ')' and locked[i] == '1':
                countCloseBracket -= 1
                countOpenBracket -= 1
            else:
                countOpenBracket -= 1
                countCloseBracket += 1
            if (countOpenBracket < 0): countOpenBracket = 0
            if (countCloseBracket < 0):
                return False
        if countOpenBracket < 0:
            return True
        if countCloseBracket < 0:
            return Fasle
        return countOpenBracket == 0