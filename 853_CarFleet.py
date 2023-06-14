class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Turn the two lists into a list of ordered pairs, [position,speed,time]
        time_list = []
        for i in range(len(position)):
            #time = distance/speed
            time_list.append((target - position[i])/speed[i])
        print(time_list)

        car_list = list(zip(position,speed,time_list))
        car_list.sort()
        car_list.reverse()

        #empty stack to add the values on
        car_stack = []


        # The intuition here is to think about the cars as linear functions. Sorting from further along the route to least we can
        # compare the time it take them to arrive at the end of the road. Pushing a value onto the stack, and comparing it with the value below it
        # if the new value takes less time than the one already on the stack, we know that it will catch up and become part of the same fleet
        # if so we can remove it from the stack as it will be identical to the one below it eventually (as it cannot pass and will have the same movement speed)
        # If not then it will be its own unique fleet and we can add it onto the stack
        # Once we have iterated through the entire list, the number of values left on the stack will be the number of fleets created
    
        for car in car_list:
            if not car_stack:
                car_stack.append(car)
            else:
                car_stack.append(car)
                #if the time is less than the other cars time, we know we catch up and can pop it off the stack and keep the slower one
                if car_stack[-1][2] <= car_stack[-2][2]: 
                    car_stack.pop()
                

            
        return len(car_stack)


