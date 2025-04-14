from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # ถ้าทั้งคู่เป็น None -> เหมือนกัน
        if not p and not q:
            return True
        # ถ้าค่าใดค่าหนึ่งเป็น None หรือค่าไม่เท่ากัน -> ไม่เหมือนกัน
        if not p or not q or p.val != q.val:
            return False
        # เช็คซ้าย และ ขวา
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 🧪 ทดสอบแบบง่าย (ต้องเขียนสร้างต้นไม้ด้วย)
if __name__ == "__main__":
    s = Solution()
    
    # Tree 1:   1
    #         / \
    #        2   3
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    print(s.isSameTree(p, q))  # ✅ True
