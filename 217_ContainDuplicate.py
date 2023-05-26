class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create a set
        int_set = set()
        #loop through the list, if the val exists in the set already return true
        for val in nums:
            if val in int_set:
                return True
            else:
                #append if not
                int_set.add(val)
        #if we reach the end of the list and there are no dupes were found then return false        
        return False        
        