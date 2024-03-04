# not turning int into string
# not using library

class Solution:

    def findFirst(f: int, curDigits: int) -> int:
        return (f // (10 ** (curDigits-1))) % 10

    def findDigits(d: int) -> int:
        num = d
        digits = 1
        while num // 10 > 0:
            num = num // 10
            digits += 1
        return digits

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        curDigits = Solution.findDigits(x)
        numLoops = curDigits / 2

        while numLoops >= 1:
            first = Solution.findFirst(x, curDigits)
            last = temp % 10

            if first != last:
                return False

            temp //= 10
            curDigits -= 1
            numLoops -= 1

        return True

    def isPalindromeBetter(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        reverse = 0

        while temp > 0:
            reverse = reverse * 10 + temp % 10
            temp //= 10

        return x == reverse


print(Solution().isPalindromeBetter(101))
