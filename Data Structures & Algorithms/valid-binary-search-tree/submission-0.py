# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]):
        currLeft = root
        currRight = root
        dp = [False]* 2
        left = 0
        right = 1

        while currLeft.left:
            if currLeft.left.val < currLeft.val and currLeft.right.val > currLeft.val:
                dp[left] = True
            currLeft = currLeft.left

        while currRight.right:
            if currRight.left.val < currRight.val and currRight.right.val > currRight.val:
                dp[right] = True
            currRight = currRight.right    

        if dp[left] == dp[right] and dp[left] == True:
            return True

        return False         
        