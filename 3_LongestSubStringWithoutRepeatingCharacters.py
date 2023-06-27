class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        # we use a slidint window approach with  a left and right pointer
        # the char set will be used to contain the characters that our window is currently enveloping
        # if we get to a character that is already inside of it, we remove from the left until that is not the case 
        l = 0
        char_set = set()
        res = 0
        
        # the r is our right side of the sliding window 
        for r in range(len(s)):
            # we found a matching character and now must remove from our set starting from the left until this is no longer true
            while s[r] in char_set:
                char_set.remove(s[l])
                #update out left pointer 
                l += 1
            # we no longer have a match or did not have one in the first place and can add the character to our set
            char_set.add(s[r])
            # we then keep checking if our set gets bigger than the max len it has been while looping through the string
            res = max(res,len(char_set))
        return res
                
        


