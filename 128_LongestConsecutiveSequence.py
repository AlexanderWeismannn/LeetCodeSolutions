class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # creates a set to avoid duplicate number in our list
        con_set = set(nums)

        # create a longest sequence val and count val for iterative checking of sequence length
        longest_sequence = 0
        # count starts at 1 since thats the min length of a sequence
        count = 1

        
        for val in nums:
            # check that we are at the start of a sequence, if not the skip to the next val
            if val-1 in con_set:
                continue
            else:
            # if we are, then while we have the next number in the sequence increment our counter
                while val+1 in con_set:
                    count+=1
                    val+=1
                # once we break our sequence compare its length to the longest sequence we've had and take the longest of the two
                longest_sequence = max(longest_sequence,count)
            # reset our counter back to 1 for the next val in the list to compare
            count=1

        return longest_sequence


                

