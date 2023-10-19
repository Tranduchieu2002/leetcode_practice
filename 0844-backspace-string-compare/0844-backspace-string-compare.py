class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def rmChars(text):
            st = []
            
            for c in text:
                if c == "#" and st:
                    st.pop()
                if c != '#':
                    st.append(c)
            print(st)
            return st
            
        return rmChars(s) == rmChars(t)
        
         
        