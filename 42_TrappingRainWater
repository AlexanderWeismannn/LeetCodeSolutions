class Solution:
    def trap(self, height: List[int]) -> int:

        # inital var creation. maxL and maxR will store the running max values found while progressing through the list f->b and b->f
        # l and r are temp storage variables 
        res = 0
        l,r = 0,0
        maxL,maxR = [],[]

        #edge case of too small of a list
        if len(height) <= 2:
            return 0

        #iterate from left to right finding the largest current values and store in maxL
        for i in range(len(height)):
            if height[i] > l:
                l = height[i]
            maxL.append(l)

        #iterate from right to left finding the largest current values and store in maxR
        for j in range(len(height)-1,-1,-1):
            if height[j] > r:
                r = height[j]
            maxR.append(r)
        
        #reverse our maxR list so that it can be iterated through using the same index step in the next for loop
        maxR.reverse()

        # loop through and find the result of taking the min(L[x],R[x]) - height[x] 
        # This works as the the index we are on itself counts as the largest L or R value
        # meaning at pos 0 with nothing to the left of it, the value there is itself the largest L
        # at pos len(list) with nothing to the right, the value itlsef is the largest R
        # we then simply take the min between the two values at index x and subtract the current height of x to see how much water can exist
        # the number can be negative so we simply only add postive values to our res 
        for k in range(len(height)):
            #makes sure we arent at the beginning or end
            val = min(maxL[k],maxR[k]) - height[k]
            if val > 0:
                res += val

        return res