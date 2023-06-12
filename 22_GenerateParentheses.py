
# This solution utlises backtracking to come up with the recusrive solution.
# The set of parentheses rules are as follows:
# 1.) There can NEVER be MORE ) than ( during the creation process
# 2.) If the number of ( and ) are the same we must alway choose to add (
# 3.) If there are more ) than ( we can choose to either add another ( or )
# 4.) If we have used all of our open brackets we must the close everything 
# this is the foundation of of recursive logic and is shown below

def recursiveGeneration(final_list,n,parenth = "", op = 0, cl = 0):
    # 2.) also we must make sure we dont create more pairings
    if op == cl and op < n:
        #add and open bracket
        recursiveGeneration(final_list,n,parenth+"(",op+1,cl)
    # 3.) also we must make sure we dont create more pairings    
    elif op > cl and op < n:
        #add another open
        recursiveGeneration(final_list,n,parenth+"(",op+1,cl)
        #add a close
        recursiveGeneration(final_list,n,parenth+")",op,cl+1)
    # 4.) reached the op limit and must now close
    elif op > cl and op == n:
        #add a close
        recursiveGeneration(final_list,n,parenth+")",op,cl+1)
    else:
        # We have created an acceptable permutation of "well-formed parentheses"
        final_list.append(parenth)
    
class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        #global list to append to during recursive solution
        final_list = []
        
        recursiveGeneration(final_list,n,"",0,0)
        return final_list
        
