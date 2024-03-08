class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqList = [0] * (101)
        maxFreq = 0
        for num in nums:
            freqList[num] += 1
            maxFreq = max(maxFreq, freqList[num])
        ans = 0
        for key in freqList:
            if key == maxFreq:
                ans += maxFreq
        
        return ans
            
            