class Solution:
    def getMaxLengthStr(strs: list[str]) -> str:
        max = strs[0]
        for i in range(1, len(strs)):
            if len(max) < len(strs[i]):
                max = strs[i]
        return max

    def longestCommonPrefix(self, strs: list[str]) -> str:
        longestStr = Solution.getMaxLengthStr(strs)
        common = ""
        for char in longestStr:
            common_count = 0
            for string in strs:
                if char in string:
                    common_count += 1
                if common_count == len(strs):
                    common += char
            # print(char, common_count, common)

        return common


result = Solution().longestCommonPrefix(["flower", "flow", "flight"])
print(result)
