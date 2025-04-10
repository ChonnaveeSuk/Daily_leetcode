class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # แบ่งคำด้วยช่องว่าง แล้วหา len ของคำสุดท้าย
        return len(s.strip().split()[-1])

# 🧪 ทดสอบตัวอย่าง
if __name__ == "__main__":
    s = Solution()

    print(s.lengthOfLastWord("Hello World"))                # ✅ 5
    print(s.lengthOfLastWord("   fly me   to   the moon  "))# ✅ 4
    print(s.lengthOfLastWord("luffy is still joyboy"))      # ✅ 6
