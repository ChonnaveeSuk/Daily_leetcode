import os

# สร้างโฟลเดอร์และไฟล์สำหรับ Day 6: Find the Index of the First Occurrence in a String
base_path = r"C:\Daily_leetcode\Day_6_StrStr_Ex28_Easy"
file_path = os.path.join(base_path, "Solution_Day6_Py.py")

# โค้ด Python สำหรับโจทย์ strStr (LeetCode #28)
code = '''\
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Return the index of the first occurrence of needle in haystack, or -1 if not found.
        """
        return haystack.find(needle)

# 🧪 ตัวอย่างทดสอบ
if __name__ == "__main__":
    s = Solution()
    print(s.strStr("sadbutsad", "sad"))    # ✅ 0
    print(s.strStr("leetcode", "leeto"))   # ✅ -1
    print(s.strStr("hello", "ll"))         # ✅ 2
'''

# สร้างไฟล์
os.makedirs(base_path, exist_ok=True)
with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

file_path
