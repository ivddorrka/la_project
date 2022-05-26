from gurobipy import *




class LP_Solutions:
    def __init__(self):
        self.model = Model();
        self.counter = 1;
    
    def set_variables(self, variable):
        self.model.addVar(name=f"{variable}")
    def set_objective_function(self, func, min_or_max_it):
        self.model.setObjective(func , min_or_max_it)
    
    def add_all_constraints(self, func):
        self.model.addConstr(func, f"c{self.counter}")
        counter += 1
    def run_optimization(self):
        self.model.optimize()



# Create a new model
m = Model()

# Create variables
x1 = m.addVar(name="x1")
x2 = m.addVar(name="x2")

# Set objective function
m.setObjective(3*x1 + 2*x2 , GRB.MAXIMIZE)

#Add constraints
m.addConstr(2.2*x1 + x2  <= 100, "c1")
m.addConstr(x2  <= 30, "c3")
m.addConstr(x1  >= 0, "c4")
m.addConstr(x2  >= 0, "c5")

# Optimize model
m.optimize()

#Print values for decision variables
for v in m.getVars():
    print(v.varName, v.x)

#Print maximized profit value
print('Maximized profit:',  m.objVal)