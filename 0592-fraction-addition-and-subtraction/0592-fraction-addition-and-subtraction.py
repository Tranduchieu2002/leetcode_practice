class Solution:
    def convert(self, expression, fractions):
        sign = 1
        temp = expression[0]

        
        n = len(expression)
        i = 0
        while i < n:
            c = expression[i]
            num = 0
            if not c.isdigit():
                if c == '+':
                    pass
                elif c == '-':
                    sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            num = num * sign
            sign = 1
            i += 1
            den = 0
            while i < n and expression[i].isdigit():
                den = den * 10 + int(expression[i])
                i += 1
            fractions.append((num, den))
        return 
    def add(self, first, second):
        numerator = first[0] * second[1] + first[1] * second[0]
        denominator = first[1] * second[1]

        common_divisor = gcd(numerator, denominator)
        numerator //= common_divisor
        denominator //= common_divisor

        return (numerator, denominator)

        
    def fractionAddition(self, expression: str) -> str:
        
        fractions = []
        self.convert(expression, fractions)
        ans = (0, 1)
        for fraction in fractions:
            
            ans = self.add(ans, fraction)
        return str(ans[0]) + '/' + str(ans[1])
        