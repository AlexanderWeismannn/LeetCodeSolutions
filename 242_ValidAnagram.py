class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # create a list we can pull values from to check against the string t
        anagram_list = []
        for i in s:
            anagram_list.append(i)
        
        # compare each char to see if there is a char in the list we can match it with. If not the string is autoatically not an anagram
        for char in t:
            if char in anagram_list:
                anagram_list.remove(char)
            else:
                return False
        
        # one last check to make sure we used all of the values in our list before returning true
        if anagram_list == []:
            return True
        else:
            return False

        
