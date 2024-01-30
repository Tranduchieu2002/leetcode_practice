class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = {
          '+':lambda a, b: a + b,
          '-':lambda a, b: a - b,
          '*':lambda a, b: a * b,
          '/':lambda a, b: int(a / b)
        }

        for t in tokens:
            if(t not in operators):
                st.append(int(t))
                continue
            val1 = st.pop()
            val2 = st.pop()
            st.append(operators[t](val2, val1))
            
        return st.pop()