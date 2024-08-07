eng = [
    "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
]

eng2 = [
    "", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
]

eng3 = ["", "Thousand", "Million", "Billion"]

class Solution:
    def numberToWords(self, num: int) -> str:
        if (num == 0):
            return "Zero"
        # convert 3 chars
        def convertAClusterChars(num):
            ans = ""
            while num > 0:
                if num >= 100:
                    w = num // 100
                    num = num % 100
                    ans += eng[w] + " Hundred "
                elif num >= 20:
                    w = num // 10
                    num = num % 10
                    ans += eng2[w] + " "
                else:
                    ans += eng[num]
                    num = 0
            return ans.strip()            
        cnt, ans = 0, ""
        while num > 0:
            words = num % 1000
            num = num // 1000
            if (words > 0):
                converted = convertAClusterChars(words) + " "+ eng3[cnt]
                ans = converted + " " + ans
            else:
                ans += convertAClusterChars(words) 
            cnt += 1
        return ans.strip()
    