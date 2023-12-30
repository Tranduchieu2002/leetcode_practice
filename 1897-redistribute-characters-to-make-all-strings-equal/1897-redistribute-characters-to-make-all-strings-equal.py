class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        letters = chain(*words)
        return not any(val % n != 0 for val in Counter(letters).values())
