# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        sortedList = []
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            sortedList.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(1, len(sortedList)):
            if sortedList[i-1] >= sortedList[i]:
                return False
        return True 