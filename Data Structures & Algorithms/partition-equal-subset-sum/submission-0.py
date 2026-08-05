class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_Sum = sum(nums)
        left = 0
        right = len(nums)-1
        currSum = 0
        while left < right:
            currSum += nums[left]
            if currSum*2 == total_Sum:
                return True
            currSum += nums[right]
            if currSum*2 == total_Sum:
                return True
            if currSum*2> total_Sum:
                currSum -= nums[right]
            left += 1
            right -= 1    
        return False        

        