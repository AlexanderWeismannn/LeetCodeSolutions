class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        # First we check the range of values in each row of the 2d array.
        # We know that if our target is not in between that range than we can skip that row
        for row in matrix:
            # If it is between that row then we aply the binary search algorithm
            if row[0] <= target <= row[-1]:
                a,b = 0, len(row)-1
                mid = int(len(row)/2)
                while a <= b:
                    if target == row[mid]:
                        return True
                    elif target < row[mid]:
                        b = mid-1
                        mid = b - int((b-a)/2)
                    elif target > row[mid]:
                        a = mid+1
                        mid =  a + int((b-a)/2)
                # if the result was not found we know that there are no other possible rows where it can be and can return false
                return False
                
            # It isnt for this one so we just skip
            else:
                continue
