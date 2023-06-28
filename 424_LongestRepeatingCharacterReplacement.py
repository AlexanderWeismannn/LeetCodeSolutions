class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #dictionary for storing the number of characters in the string for each unique char
        count = {}
        res = 0
        l=0

        for r in range(len(s)):
            # update the value of the key or initialize it
            count[s[r]] = count.get(s[r],0) + 1
            #length of our window
            w_length = (r-l)+1
            # if the length - most frequent char > k we know we have an invalid window and need to move it EX: k=1 AABAB 5-3 = 2 > 1 => invalid
            if w_length - max(count.values()) > k:
                #minus 1 from that chars count and move the left pointer of the window right 
                count[s[l]] -= 1
                l+=1
            #check for new max window size every iteration
            res = max(res,(r-l)+1)
            
        return res