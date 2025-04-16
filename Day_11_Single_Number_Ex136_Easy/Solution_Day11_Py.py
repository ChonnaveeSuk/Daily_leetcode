class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ใช้ XOR: a^a = 0, a^0 = a
        result = 0
        for num in nums:
            result ^= num
        return result

# 🧪 ตัวอย่างทดสอบ
if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 1]))          # ✅ 1
    print(s.singleNumber([4, 1, 2, 1, 2]))    # ✅ 4
    print(s.singleNumber([1]))               # ✅ 1
