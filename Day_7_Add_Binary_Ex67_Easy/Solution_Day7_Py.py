class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # แปลงเป็น int ฐาน 2 → บวก → แปลงกลับเป็น binary string
        return bin(int(a, 2) + int(b, 2))[2:]

# 🧪 ตัวอย่างทดสอบ
if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11", "1"))       # ✅ "100"
    print(s.addBinary("1010", "1011"))  # ✅ "10101"
    print(s.addBinary("0", "0"))        # ✅ "0"
