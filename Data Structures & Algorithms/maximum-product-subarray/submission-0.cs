public class Solution {
    public int MaxProduct(int[] nums) {
        int res = 0;
        int curMin = 1;
        int curMax = 1;

        foreach (int num in nums){
            int temp = num * curMax;
            curMax = Math.Max(Math.Max(num*curMax, num*curMin),num);
            curMin = Math.Min(Math.Min(temp, num*curMin), num);
            res = Math.Max(res, curMax);
        }
        return res; 
        
    }
}
