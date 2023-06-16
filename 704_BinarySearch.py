class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # we create 3 pointers, one to the start, one to the end and one to the middle of the list 
        a,b = 0,len(nums)-1
        mid = int(len(nums)/2)

        # we then perform the binary search alg. the while loop will end if at any point the a and b overlap
        # since this means that our reduction has finished and no target was found
        while a <= b:
            # if we found the answer we return its index
            if nums[mid] == target:
                return mid
            # if the midpoint value is bigger than our target we move our b value to the midpoint - 1 for our new range and calculate our new mid by taking the distance between
            # a and b and minusing that from our b
            elif nums[mid] > target:
                b = mid-1
                mid = b - int((b - a)/2)
            # if the midpoint is smaller than our target we update the a equal to our midpoint + 1 for our new range and calculate our new mid by taking the distancve between
            # a and b and adding that to our a
            elif nums[mid] < target:
                a = mid + 1
                mid = a + int((b - a)/2)

        # if we never foud our target we return -1
        return -1