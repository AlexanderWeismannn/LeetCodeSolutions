class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # mimic a list from 1 to the max pile value. This will allow us to to perform binary sort on all possible numbers rather than
        # iterating through one at a time. Turning O(n) -> Olog(n)
        # this is more time and space efficient than creating an actual list of all values from 1 to max value of piles
        l,r = 1, max(piles)
        res = r

        #classic binary search while loop
        while l <= r:
            # k is our midpoint, will constantly update it each loop
            k = (l+r)//2
            hours = 0

            # check how many total hours it will take to consume all piles of bananas
            for p in piles:
                hours += int(math.ceil(p/k))
                
            # if it takes fewer or the same amount of hours as h to eat all bananas, set the current res = min of the res and our k value
            # also we know that the hours are less so we can keep reducing and see if another smaller value k still works
            if hours <= h:
                res = min(res,k)
                r = k-1
            # if it takes more hours than h to eat all the bananas we know our k value is too small and needs to be increased
            # update the binary search parameters accordingly
            elif hours > h:
                l = k+1

        return res

