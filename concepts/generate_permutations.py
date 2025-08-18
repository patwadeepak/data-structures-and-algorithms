def generate_permutations(nums):
    result = []
    def backtrack(current_permutation, remaining_nums):
        # Base case: if the permutation is complete, add it to the result
        if not remaining_nums:
            result.append(list(current_permutation))
            return
        
        # Recursive step: try all remaining numbers
        for i in range(len(remaining_nums)):
            # Choose a number
            num_to_add = remaining_nums[i]
            current_permutation.append(num_to_add)
            
            # Create a new list for the remaining numbers
            new_remaining = remaining_nums[:i] + remaining_nums[i+1:]
            
            # Recurse with the new state
            backtrack(current_permutation, new_remaining)
            
            # Backtrack: remove the last added number
            current_permutation.pop()

    backtrack([], nums)
    return result

# Example usage
nums = [1, 2, 3]
permutations = generate_permutations(nums)
print(permutations)
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
