class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #impossible to have permutation on the second string if our first string is longer
        if len(s1) > len(s2):
            return False
        
        # create alphabet character lists
        char_set_s1,char_set_s2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            char_set_s1[ord(s1[i]) - ord('a')] += 1
            char_set_s2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        # we know the array will be 26 spaces long that we loop through and see what our matches are based on the window we have created of length s1
        for j in range(26):
            matches += (1 if char_set_s1[j] == char_set_s2[j] else 0)

        l = 0
        for r in range(len(s1),len(s2)):

            if matches == 26:
                return True

            # check our new r
            index = ord(s2[r]) - ord('a')
            char_set_s2[index] += 1
            # we incremented and check if we've found a match
            if char_set_s1[index] == char_set_s2[index]:
                matches += 1
            # we need to check that we also didnt use to have a match and ruined it
            elif char_set_s1[index] + 1 == char_set_s2[index]:
                matches -= 1    

            # move our l
            index = ord(s2[l]) - ord('a')
            char_set_s2[index] -= 1

            if char_set_s1[index] == char_set_s2[index]:
                matches += 1
            elif char_set_s1[index] - 1 == char_set_s2[index]:
                matches -= 1

            l+=1

        return matches == 26