class Solution:
    def maxProduct(self, nums: List[int]) -> int: 
        leftProd = 1
        rightProd = 1
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        left = 0
        right = len(nums) - 1

        while right > -1:
            leftProd *= nums[left]
            rightProd *= nums[right]

            prefix[left] = leftProd
            suffix[right] = rightProd

            if prefix[left] == 0:
                leftProd = 1
            if suffix[right] == 0:
                rightProd = 1  

            left += 1
            right -= 1

        return max(max(suffix), max(prefix))  


        