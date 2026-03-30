class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(index, remaining_sum, current_combination, all_combinations):
            """
            Explore all combinations using binary choice: TAKE or SKIP
            
            Args:
                index: Current position in candidates array
                remaining_sum: How much more we need to reach target
                current_combination: Coins we've picked so far
                all_combinations: List to store all valid combinations
            """
            
            # Base case 1: Went past array OR sum became negative
            if index >= len(candidates) or remaining_sum < 0:
                return
            
            # Base case 2: Found exact target! 🎯
            if remaining_sum == 0:
                all_combinations.append(current_combination.copy())
                return
            
            # CHOICE 1: TAKE the current coin (can use it again)
            current_combination.append(candidates[index])
            backtrack(
                index,  # Stay at same index (can reuse this coin)
                remaining_sum - candidates[index],  # Subtract coin value
                current_combination,
                all_combinations
            )
            current_combination.pop()  # Undo the choice (backtrack)
            
            # CHOICE 2: SKIP the current coin (move to next)
            backtrack(
                index + 1,  # Move to next coin
                remaining_sum,  # Sum unchanged
                current_combination,
                all_combinations
            )
        
        # Initialize and start the search
        all_combinations = []
        backtrack(0, target, [], all_combinations)
        return all_combinations