class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # ใช้ pointer แทนตำแหน่งที่จะเก็บค่าที่ไม่ใช่ val
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# 🧪 ตัวอย่างการทดสอบ
if __name__ == "__main__":
    s = Solution()

    nums = [3, 2, 2, 3]
    k = s.removeElement(nums, 3)
    print(k, nums[:k])  # ✅ Expected: 2, [2, 2]

    nums = [0,1,2,2,3,0,4,2]
    k = s.removeElement(nums, 2)
    print(k, nums[:k])  # ✅ Expected: 5, [0,1,3,0,4]
