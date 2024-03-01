class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqStr = []
        for s in s:
            if s is not in uniqStr:
                uniqStr.append(s)
        

Solution().lengthOfLongestSubstring("asdasdbb")