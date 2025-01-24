class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Initialize a pointer for the position of non-val elements
        k = 0
        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != val:
                # Place the non-val element at the current pointer and increment k
                nums[k] = nums[i]
                k += 1
        # Return the count of non-val elements
        return k
