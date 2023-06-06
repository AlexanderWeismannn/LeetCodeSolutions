class Solution:
    def maxArea(self, height: List[int]) -> int:

        # initial pointer positions at the beginning and end of the array
        l,r = 0,(len(height)-1)
        # initial max area value to compare, min of the two heights * the distance between the two lines
        max_area = min(height[l],height[r])*(len(height)-1)

        # while loop through and adjust poitners as needed
        while l < r:
            if height[l] < height[r]:
                l += 1 
            elif height[l] > height[r]:
                r -= 1
            else:
                # you can move both pointers, as moving one will guarantee a smaller area than what was previously taken. Since even if the next line is taller
                # the minimum will still be the same as the previous iteration but with a smaller distance between the lines. Resulting in a smaller area. 
                l += 1
                r -= 1
                
            # calculate the area based on the min height of the two lines and the distance between eachother
            area = min(height[l],height[r])*(r-l)
            # set the new max_area value 
            max_area = max(max_area,area)

        return max_area