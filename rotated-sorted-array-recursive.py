class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(nums, target, start, end):
            if start > end: return -1
            mid = start + (end-start)//2
            if nums[mid] == target: return mid
            
            if nums[mid] < target:
                return helper(nums, target, mid+1, end)
            elif nums[mid] > target:
                return helper(nums, target, start, mid-1)
            
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            
            if nums[mid] == target: return mid
            if nums[mid] <= nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    return helper(nums, target, mid+1, right)
                else:
                    right = mid - 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    return helper(nums, target, left, mid-1)
                else:
                    left = mid + 1
        return -1
    
    
