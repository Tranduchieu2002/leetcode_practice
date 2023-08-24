class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        ans = []
        i = 0 # index of strs
        while i < n:
            cur_s = words[i]
            cur_len = len(cur_s)
            j = i + 1
            #  j - i whitch mean the min spacing need to 
            while j < n and cur_len + len(words[j]) + j - i <= maxWidth:
                cur_len += len(words[j])
                j += 1
            
            num = j - i
            sub_ans = cur_s
            print(i , j - 1,num, cur_len)
            # 0 2 8 16
            # 3 5 13
            # 6 6 14
            if j == n or num == 1: # end or single word line
                for k in range(i + 1, j):
                    sub_ans += ' ' + words[k]
                sub_ans += ' ' * (maxWidth - len(sub_ans))
            else:
                spacing_needed = maxWidth - cur_len
                space_for_each = (spacing_needed // (num - 1))
                extra_space = spacing_needed % (num - 1)
                for k in range(i + 1, j):
                    spaces = space_for_each + int(extra_space > 0)
                    extra_space -= 1
                    sub_ans += ' ' * spaces + words[k]

            ans.append(sub_ans)
            i = j
        return ans

                