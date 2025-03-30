class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def get_pivot(nums, first, last):
            pivot = nums[first]
            left, right = first + 1, last
            while True:
                while left <= right and nums[left] <= pivot:
                    left += 1
                while left <= right and nums[right] >= pivot:
                    right -= 1
                if left > right:
                    break
                nums[left], nums[right] = nums[right], nums[left]
            nums[first], nums[right] = nums[right], nums[first]
            return right
        
        def quick_sort(nums, first, last):
            if first < last:
                pivot = get_pivot(nums, first, last)
                quick_sort(nums, first, pivot-1)
                quick_sort(nums, pivot+1, last)
        
        quick_sort(nums, 0, len(nums)-1)