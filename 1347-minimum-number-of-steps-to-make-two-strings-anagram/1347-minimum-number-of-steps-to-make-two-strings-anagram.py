class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict_word_s = defaultdict(int)
        dict_word_t = defaultdict(int)        
        for i in range(len(s)):
            dict_word_s[s[i]] += 1
            dict_word_t[t[i]] += 1            
        ans = 0
        # print(dict_word_s, dict_word_t)
        for key in s:
            if dict_word_s[key] > dict_word_t[key]:
                ans += dict_word_s[key] - dict_word_t[key]
            dict_word_s[key] = 0
            # dict_word_t[key] = 0
        
        return ans