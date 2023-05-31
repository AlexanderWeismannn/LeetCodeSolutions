class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # calculate prefix, cumulative product of all the values before and including the current position (left -> right)
        prefix = [nums[0]]*len(nums)
        for i in range(1,len(nums)):
            prefix[i] = nums[i] * prefix[i-1]
        

        # calculate postfix, cumulative value of all the values after and including the current position (right -> left)
        postfix = [nums[-1]]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            postfix[i] = nums[i] * postfix[i+1]
    
        # add buffers to the prefix and postfix so the pre/post calculation can be done
        prefix.insert(0,1)
        postfix.append(1)

        # multiply the value before on the prefix position and the value after on the postfix position to the index to get the product.
        # Using the buffers we can stay and the current index for the prefix and only need to +1 for the post fix index
        answer = []
        for j in range(0,len(nums),1):
            answer.append(prefix[j] * postfix[j+1])

        return answer
