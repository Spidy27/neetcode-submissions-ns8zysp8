class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        leftProd = 1
        rightProd = 1
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        max_prod = 0
    
        for i in range(len(nums)):
            leftProd *= nums[i] 
            prefix[i] = leftProd
            rightProd *= nums[-i]
            suffix[i] *= rightProd

        return max(max(prefix), max(suffix))


        