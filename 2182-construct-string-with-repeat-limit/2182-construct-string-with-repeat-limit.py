class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = collections.Counter(s)
        chars = [(-ord(k), k, v) for k, v in cnt.items()]

        heapq.heapify(chars)
        res = []
        while chars:
            o, ch, ct = heapq.heappop(chars)
            add = 0
            if len(res) >= repeatLimit and res[-1] == ch:
                if not chars: break
                no, nch, nct = heapq.heappop(chars)
                res.append(nch)
                if nct - 1 != 0: heapq.heappush(chars, (no, nch, nct - 1))
            else:
                add = min(repeatLimit, ct)
                res.extend([ch for _ in range(add)])
            if ct - add != 0: heapq.heappush(chars, (o, ch, ct - add))
        return "".join(res)