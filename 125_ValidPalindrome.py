class Solution:
    def isPalindrome(self, s: str) -> bool:

        # custom alphanumeric checker method. Could use pythons built in function buyt this was more interesting
        def isAlphaNumeric(c):
            if (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
                return True
            else:
                return False

        # takes in the original string, strips the non-alphanumeric character and sets everything to lowercase for later comparison
        pre_processed = ""
        for c in s:
            if isAlphaNumeric(c):
                pre_processed += c.lower()
            

        # helper vars, referencing the start of the string, the end of it, and get the length of it and dividing it by two to get the number of times we'll
        # need to iterate. We only need to iterate n/2 times because we are stepping forward and backwards with the two seperate pointers
        start = 0
        end = len(pre_processed) - 1
        iterate = int(len(pre_processed)/2)

        # checking that each pairing are equivalent. If not then it isnt a palindrome
        for i in range(iterate):
            if pre_processed[start] != pre_processed[end]:
                return False
            # move the pointers
            start+=1
            end-=1

        return True

