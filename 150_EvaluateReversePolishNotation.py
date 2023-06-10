class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        # We use the stack here because the pattern that the RPN has means when we see a non number value, we apply the operator to the two previous values.
        # This means that when we run into an operator, we pop the two values, perform the operation, then append the new value back onto the stack.

        for i in range(len(tokens)):

            if tokens[i] == "+":
                # apply + to the previous two values or 1 previous and the total
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(a + b)

            elif tokens[i] == "-":
                # apply - to the previous two values or 1 previous and the total
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(b - a)

            elif tokens[i] == "*":
                # apply * to the previous two values or 1 previous and the total
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(a * b)

            elif tokens[i] == "/":
                # apply / to the previous two values or 1 previous and the total
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(int(b/a))
 
            else:
                # it is simply a number and we add it to the stack
                num_stack.append(int(tokens[i]))

        # there should be no extra numbers left on the stack by the end. Simply just the answer so we return pos 0 of the stack as the answer
        return num_stack[0]
        
