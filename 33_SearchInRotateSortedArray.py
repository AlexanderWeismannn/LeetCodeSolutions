class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0,len(nums)-1
        
        while l <= r:

            m = (l+r)//2

            if nums[m] == target:
                return m

            # we are in the left side
            if nums[l] <= nums[m]:
                # check our target is greater than or less than left, if so move the left pointer right
                if target > nums[m] or target < nums[l]:
                    l = m+1
                # other wise move the right pointer left
                else:
                    r = m-1

            # we are in the right side
            else:
                # check of our target is less than the mid or greater than the right, if so move our right pointer left
                if target < nums[m] or target > nums[r]:
                    r = m-1
                # other wise move the left pointer right
                else:
                    l = m+1

            
        return -1