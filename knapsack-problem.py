from simpleai.search import SearchProblem, genetic, hill_climbing , hill_climbing_random_restarts
from simpleai.search.viewers import WebViewer, ConsoleViewer, BaseViewer
import random
from itertools import product
import secrets

my_viewer = ConsoleViewer()

weights = [ ]
values = [ ]

knapsackCapacity = []
numberOfItems = []
action_list = []
random_state = []

class KnapsackProblem(SearchProblem):  
        

        def actions(self,state):

            return action_list
               
        def result(self, state, action):
            
            if(self.value(action) >= self.value(state) and self.weight(action) <= knapsackCapacity):

                return action

            elif(self.value(state) > self.value(action) and self.weight(action) <= knapsackCapacity):

                return state
            
            else:
                
                return self.generate_random_state()
                        
        def generate_random_state(self):
            randomState = []
            valid = False

            while valid == False:
                randomState = []
                for i in range(0, numberOfItems): 
                    randomState.append(random.randint(0,1))
                valid = self.valid(randomState)

            return randomState
            

        def value(self, state):
            value = 0

            for i in range(0, numberOfItems):
                if(state[i] == 1):
                    value = value + values[i]

            return value

        def weight(self, state):
            weight = 0
                
            for i in range(0, len(state)):
                if(state[i] == 1):
                    weight = weight + weights[i]
                        
            return weight
            
        def valid(self, state):
            if self.weight(state) > knapsackCapacity:
                return False
            return True

knapsackCapacity = int(input("Please enter knapsack capacity : " ))
numberOfItems = int(input("Please enter number of items : " ))

for i in range(0,numberOfItems):

    weight = int(input("Please enter weight of item " + str(i+1) + ": "))
    weights.append(weight)

    value  = int(input("Please enter value of item " + str(i+1) + ": "))
    values.append(value)

action_list = list(product([0,1], repeat=numberOfItems))
    
problem =  KnapsackProblem()
iterations_limit = int(input("Please write Itertions Limit: "))
restarts_limit =  int(input("Please write Restarts Limit: "))
result = hill_climbing_random_restarts(problem, restarts_limit, iterations_limit, viewer=my_viewer)

print()
print("Final State: " + str(result.state))        
print('Weight = ' + str(problem.weight(result.state)))
print('Value = ' + str(result.value))
print()


input("Press a button for quit...")
