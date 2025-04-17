class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # ปรับ offset เป็น 0-based
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26
        return result

# 🧪 ตัวอย่างทดสอบ
if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(1))    # ✅ "A"
    print(s.convertToTitle(28))   # ✅ "AB"
    print(s.convertToTitle(701))  # ✅ "ZY"
