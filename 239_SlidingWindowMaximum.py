class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #solution here implements a deque (monotonic decreasing queue)
        output = []
        # this deque will contain the index of the values rather than the values themselves
        q = collections.deque()
        l,r = 0,0

        while r < len(nums):
            #keep popping values until the right most deque value is not smaller than nums[r]
            while q and nums[q[-1]] < nums[r]:
                q.pop() 
            q.append(r)

            # if our current l index is greater than the left most index in our deque we need to pop it because it is out of scope of our sliding window
            if l > q[0]:
                q.popleft()

            # since we start at l,r == 0, we can only append values to our final output once we reach the correct window size i.e. atleast k
            if (r + 1) >= k:
                # we've reach k size and can append our left most value
                output.append(nums[q[0]])
                # we only increment right if our window is >= to k
                l += 1

            # we increment right every time
            r += 1
        return output


