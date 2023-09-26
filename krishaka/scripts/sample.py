import numpy as np
from itertools import tee
a = int(input())
b = int(input())
distance = np.linalg.norm(np.array(b) - np.array(a))
#print(distance)

k = tee(a)
print(k)