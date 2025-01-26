class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)  # If the array has 2 or fewer elements, return as is.

        # Initialize the slow pointer
        slow = 2  # Start at index 2 since first two elements are always allowed
        
        # Iterate through the list with the fast pointer
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:  # Allow only two occurrences
                nums[slow] = nums[fast]
                slow += 1  # Move slow pointer

        return slow  # First 'slow' elements of nums are the modified array
