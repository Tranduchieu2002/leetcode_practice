class Solution:
    def sortVowels(self, s: str) -> str:
        def isVowel(c):
            return c.lower() in ['a', 'e', 'i', 'o', 'u']

        n = len(s)
        arr_vowels = []
        result_list = list(s)

        for i in range(n):
            if isVowel(s[i]):
                arr_vowels.append(s[i])

        arr_vowels.sort()

        for i in range(n):
            c = s[i]
            if isVowel(c):
                result_list[i] = arr_vowels.pop(0)

        return ''.join(result_list)
