class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        index = 0
        ans = ''
        while index <= 12:
            # 注意：这里是等于号，表示尽量使用大的"面值"
            while num >= nums[index]:
                num -= nums[index]
                ans += romans[index]
            index += 1
        return ans

def execute():
    num = 509
    sol = Solution()
    print(sol.intToRoman(num))

if __name__ == "__main__":
    execute()
