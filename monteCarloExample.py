import random
import math

trials = int(input("How many trials? "))
random.seed()
inside = 0

for trial in range(trials):
    x = random.random()
    y = random.random()
    radius = math.hypot(x, y)
    if radius <= 1.0:
        inside += 1

print(inside / trials * 4)
