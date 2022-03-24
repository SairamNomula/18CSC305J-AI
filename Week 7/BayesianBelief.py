# Import required packages
import math
from pomegranate import *
 
guest = DiscreteDistribution({'A': 1./3, 'B': 1./3, 'C': 1./3})
 
vehicleType = DiscreteDistribution({'A': 1./3, 'B': 1./3, 'C': 1./3})
 
# a=1
# b=1-4
# c=4-6
 
 
driver = ConditionalProbabilityTable(
    [['A', 'A', 'A', 1.0],
     ['A', 'A', 'B', 0.0],
        ['A', 'A', 'C', 0.0],
        ['A', 'B', 'A', 0.0],
        ['A', 'B', 'B', 1.0],
        ['A', 'B', 'C', 0.0],
        ['A', 'C', 'A', 0.0],
        ['A', 'C', 'B', 0.0],
        ['A', 'C', 'C', 1.0],
        ['B', 'A', 'A', 1.0],
        ['B', 'A', 'B', 0.0],
        ['B', 'A', 'C', 1.0],
        ['B', 'B', 'A', 0.5],
        ['B', 'B', 'B', 1.0],
        ['B', 'B', 'C', 0.5],
        ['B', 'C', 'A', 1.0],
        ['B', 'C', 'B', 0.0],
        ['B', 'C', 'C', 1.0],
        ['C', 'A', 'A', 1.0],
        ['C', 'A', 'B', 1.0],
        ['C', 'A', 'C', 0.0],
        ['C', 'B', 'A', 1.0],
        ['C', 'B', 'B', 1.0],
        ['C', 'B', 'C', 0.0],
        ['C', 'C', 'A', 0.5],
        ['C', 'C', 'B', 0.5],
        ['C', 'C', 'C', 1.0]], [guest, vehicleType])
 
d1 = State(guest, name="guest")
d2 = State(vehicleType, name="prize")
d3 = State(driver, name="monty")
 
network = BayesianNetwork()
network.add_states(d1, d2, d3)
network.add_edge(d1, d3)
network.add_edge(d2, d3)
network.bake()
 
beliefs = network.predict_proba({'guest': 'B', 'driver': 'B'})
print("n".join("{}t{}".format(state.name, str(belief))
      for state, belief in zip(network.states, beliefs)))