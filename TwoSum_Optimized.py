class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # create an empty dict to hold the key(number) and value(index) pairs
        twoSumDict = {}

        # generates a key and value pair from the nums list. This updates the value of duplicate numbers
        # since it will overwrite the value if it exists more than once (i.e. [2,1,1,1]) => {2:0,1:3}
        for i in range(len(nums)):
            twoSumDict[nums[i]] = i
        
        #for loop through each number in the list and see if (target - itself) exists in the dict. 
        #if yes then return the index we are at and the value to find index as a list [j,twoSumDict[vtf]]
        for j in range(len(nums)):
            vtf = target - nums[j]#value to find
            #make sure that there is a pairing and that it doesnt use itself twice
            if vtf in twoSumDict and j != twoSumDict[vtf]:
                return [j,twoSumDict[vtf]]

        #the question assumes exactly one solution so no need for edge cases
