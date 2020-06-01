import numpy as np

inputs = [1,2,3,2.5]
weights = [0.2,0.8,-0.5,1.0]
bias = 2

output = np.dot(inputs,weights)+bias
# As i have inputs first to get the desired result but if we have weights as matrix form then weights will be first otherwise we have shape error bcz with weights frist we get weights list[1].input and so on
print(output)
