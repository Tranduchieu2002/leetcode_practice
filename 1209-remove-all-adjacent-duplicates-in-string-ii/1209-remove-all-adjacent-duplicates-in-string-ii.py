class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = [('', 0)]
        for c in s:
            
            top = st[-1]
            if top[0] == c:
                st[-1] = (c, top[1] + 1)
                if st and st[-1][1] == k:
                    st.pop()
            else:
                st.append((c, 1))
            
        return ''.join(cnt * c for c, cnt in st)