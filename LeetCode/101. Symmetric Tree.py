class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def equal_check(l, r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            return equal_check(l.left, r.right) and equal_check(l.right, r.left)

        return equal_check(root.left, root.right)