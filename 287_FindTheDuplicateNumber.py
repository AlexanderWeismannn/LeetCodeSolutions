class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # This solution requires the use of:
        # Floyds algorithm until they match
        # after this create a new slow pointer that iterates
        # until it and the original slow are equal. Once this
        # is true then we know that said value is the duplicate

        # original slow and fast pointers
        slow,fast = 0,0
        while True:

            #the val in the array is the next index to traverse to
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # second slow pointer that we compare
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
