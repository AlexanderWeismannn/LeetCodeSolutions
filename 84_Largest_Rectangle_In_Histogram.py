class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # values added will look like this [position,height]
        stack = []
        largest_area = 0

        for i,h in enumerate(heights):
            # new start position for the values to be extended back from, defaults to our current index
            start = i
            # if we have values in the stack and the head is greater than our current indexs height, we pop it off the stack and calculate it potential area
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                # we take the index it had in the list - where we currently are at to get the total area of the rectangle of that height we could have made
                # i is where we are (i.e. the value that is less than our head), index is the position where the head was in our list. Getting the difference
                # of this will give us the length, after that we just multiply it by the height to get our largest area with that height.
                largest_area = max(largest_area, (i - index) * height)
                # we set start = to index because we can create a rectangle all the way back to the start position of the heads index since the current height we
                # obtained from our h is smaller than the heads. This extends the starting index of our new value we will append on back to the popped values origin.
                start = index
            # we then append the new value, if the new value is bigger than our current head then we also just append it
            stack.append([start,h])

        # once we are done there may be values left in the stack, these we rectangles that were able to be extended all the way to the end of our list 
        for i,h in stack:
            # we check each ones length taking the length of our list - its starting point * its height to see if its area id greater than the largest area we found going through
            # our list the first time
            largest_area = max(largest_area, h * (len(heights)-i))
            
        return largest_area    
        


