class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # create a list for all of the daily temp values, defaulting them to 0 incase a day doesnt exist that has a larger value than it
        res = [0] * len(temperatures)
        stack = [] # will have the index and the temp [i,temp]


        # We loop through each value in the list
        for i, temp in enumerate(temperatures):
            # Check if there is a value on the stack. If so then while the current index we are ons temp is higher than the top of the stack
            # pop it, and get the difference in the current index and the stack values index (i - stack_i). This represents the distance between
            # its original index and the new hotter temperature. This can iterate until the stack is empty or 
            while stack and temp > stack[-1][1]:
                stack_index,stack_temp = stack.pop()
                res[stack_index] = i - stack_index
            # We append at the end not matter what and this also takes into account when we have an empty stack
            stack.append([i,temp])

        return res