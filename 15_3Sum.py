class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # a + b + c == 0
        # 1.) sort the list in increasing order
        # 2.) choose a value a, if we're at the beginning no need to check for duplicate
        # 3.) perform two sum opration to find the remaining b and c values
        #   - if the sum is < 0  increment start, if the sum is > 0 decrement stop
        #   - if its equal, add to the list, then increment start automatically. IF new start is a duplicate, keep incrementing
        # 4.) return the triplets list

        # answer list
        triplets = []

        # sort the list
        nums.sort()

        # loop through each value in sorted_nums, this will be our a value
        for i, a in enumerate(nums):

            # we skip duplicate a values in our list
            if i > 0 and a == nums[i-1]:
                continue
            # we are not at the first position in our list anymore
            else:

                # the start and stop values represent the left and right pointers at the beginning and end of our sorted list.
                start = i+1
                stop = (len(nums)-1)

                # same logic as two sum 2 where we use pointers
                while(start < stop):
                    three_sum = a + nums[start] + nums[stop]
                    # if our total is too big decrease stop
                    if three_sum > 0:
                        stop -= 1
                    # if our total is to small increase start
                    elif three_sum < 0:
                        start += 1
                    # combination found, so add it to the triplets list
                    else:
                        # we found a solution that works so we add it to the list 
                        triplets.append([a,nums[start],nums[stop]])
                        # there can be more so we update the start pos by 1 to continue
                        start += 1

                        # !--- IMPORTANT ---! 
                        # we also have to check that the new start pos value isnt a duplicate
                        # if it is we keep indexing until we either find a new start point or overlap with stop
                        # this only needs to be done with the start pointer and not the stop since this eliminates potential duplicate triplets
                        while nums[start] == nums[start-1] and start < stop:
                            start += 1

        return triplets
