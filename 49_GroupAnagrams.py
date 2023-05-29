class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a default dict where the values are a list by default that we can append to during our for loop
        ang_dict = defaultdict(list)

        # edge cases
        # empty input list
        if strs == [""]:
            return [[""]]
        # contains only 1 value
        if len(strs) == 1:
            return[strs]

        # create a list that will map the number of letters used to a position from 0-25 // 0 => a 25 => z
        # Example: (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
        for val in strs:
            count = [0] * 26
            for char in val:
                #int value of char - position 0 || i.e. ord("b") - ord("a") = 1
                count[ord(char) - ord('a')] += 1
            # count now becomes a unique key that all anagrams share in common. We use it as a tuple / key and append the associated value
            # to the list 
            ang_dict[tuple(count)].append(val)

        # grab all the value pairs from the dict and return the answer
        res = ang_dict.values()
        return res

