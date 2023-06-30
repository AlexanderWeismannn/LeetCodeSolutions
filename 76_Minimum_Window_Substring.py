class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # edge case if our t is empty or s and t are the same
        if t == "":
            return ""
        
        # using dictionary comprehension we generate a dict with each characters occurence for t and an empty one for our window
        t_dict = {char: t.count(char) for char in t}
        window = {}

        # we get the len of the t_dict for need as its the number of matches we need to know not the length og our string 
        have,need = 0, len(t_dict)
        #res_len stores the shortest substring and res stores their index (window l and window r)
        res_len = float('infinity')
        res = [-1,-1]
        #left part of our sliding window 
        l = 0

        # right part of our sliding
        for r in range(len(s)):
            char = s[r]
            #update our dict to either create a new key or increase the curernt one
            window[char] = 1 + window.get(char,0)

            # We now have a match and can update our have value by one
            if char in t_dict and window[char] == t_dict[char]:
                have += 1
            
            # Now check if have == need and get the length
            while have == need:
                # store its length and index values if its smaller
                if (r-l+1) < res_len:
                    res = [l,r]
                    res_len = (r-l+1)
                #try to minimize string
                window[s[l]] -= 1
                #check if we lose a have value
                if s[l] in t_dict and window[s[l]] < t_dict[s[l]]:
                    have -= 1
                # move our left pointer of the window over
                l+=1

        return s[res[0]:res[1]+1] if res_len != float('infinity') else ""




