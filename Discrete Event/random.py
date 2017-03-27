import random
import math

random.seed()
for x in range(20):
    r = random.random() # [0,1)
    x = -1/math.log(r)
    print(x)
