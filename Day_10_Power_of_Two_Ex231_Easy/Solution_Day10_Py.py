class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # จำนวนที่เป็น Power of Two จะมีเพียง 1 bit ที่เป็น 1 ในฐานสอง (n > 0 and n & (n-1) == 0)
        return n > 0 and (n & (n - 1)) == 0

# 🧪 ตัวอย่างทดสอบ
if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfTwo(1))    # ✅ True  (2^0)
    print(s.isPowerOfTwo(16))   # ✅ True  (2^4)
    print(s.isPowerOfTwo(3))    # ✅ False
    print(s.isPowerOfTwo(64))   # ✅ True
    print(s.isPowerOfTwo(0))    # ✅ False
