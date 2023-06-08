class Solution:
    def isValid(self, s: str) -> bool:

        # We create a parenthese dict for use by the stack when looping through the string
        # the stack functionality will come into play when we start looping
        paren_dict = {"(":")","[":"]","{":"}"}
        stack = []

        #quick edge case check to make sure we actually have at least 2 parentheses to compare
        if len(s) < 2:
            return False

        # The trick used here is that when we see an open bracket we place its closed counterpart on the stack
        # we know that eventually we will need a closed counterpart in the string we are looping through to have a valid
        # parenthese. It will also need to close in the correct order (I.E. the most recent open parenthese will be the first to close)
        # This logic fits perfectly into the stack data structure (FILO).
        for c in s:
            # if its an open parenth we add its closed counterpart onto the stack
            if c in paren_dict:
                stack.append(paren_dict[c])
            # if we encounter a closed one we check to see if there exists a value in the stack to compare and that the top of the stack matches it (meaning that this is the correct match order)
            # if yes we pop it from the stack
            elif stack and c == stack[-1]:
                stack.pop()
            # if not then there is no way this can be a valid set of parentheses so we can return False immidiately
            else:
                return False
        
        # If the stack isnt empty when we are done then we know that either the order of open/closing parenthese are wrong or there werent an equal amount
        if len(stack) == 0:
            return True
        else:
            return False
        
