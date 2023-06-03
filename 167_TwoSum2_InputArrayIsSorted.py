class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # our two pointers in our list, start being the beginning, stop being the end
        start = 0
        stop = (len(numbers)-1)

        #we loop through while start hasnt reached the end
        # Using the fact that our list is sorted already in ascending order, we know that if the sum is
        # greater than our target we can decrement our stop pointer because no other combination of start +  current stop
        # index will gives us the target value we want. Conversly, if the sum is smaller than our target we apply the same logic
        # and increment our start pointer 
        while(start < len(numbers)):
            if (numbers[start] + numbers[stop]) > target:
                stop -= 1
            elif (numbers[start] + numbers[stop]) < target:
                start += 1
            else:
                # the problem wants us to return the index + 1
                return [start+1,stop+1]
            
                