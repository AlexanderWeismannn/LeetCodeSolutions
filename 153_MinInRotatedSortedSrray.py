class Solution:
    def findMin(self, nums: List[int]) -> int:

        # our left pointer, right pointer, and result (defaulted to some arbitrary numberin the nums list)
        l,r = 0,len(nums)-1
        res = nums[l]

        # while the pointers have crossed over eachother
        while l <= r:

            # check if we are fully in a sorted part of the list (i.e. 1,2,3,4)
            if nums[l] < nums[r]:
                # we are so we can get the min value and break the loop
                # This is because we will have already crossed the pivot point 
                res = min(res,nums[l])
                break
            
            # otherwise generate the new midpoint 
            m = (l+r)//2

            # if the mid val is greater than the left val, we know we need to go right until we find the pivot and nums[L] < nums[R] 
            if nums[m] >= nums[l]:
                # compare our left val with the current res and update it before moving our left pointer to the right of mid.
                res = min(res,nums[l])
                l = m+1
            # else our mid val is less than our left val, so we want to keep going left until we find the smallest value
            else:
                r = m-1
                res = min(res,nums[m])

        return res     

