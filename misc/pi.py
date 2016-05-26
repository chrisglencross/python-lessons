import random

c = 0
d = 0

for count in range(0, 100000000):
    c=c+1
    x = random.random()
    y = random.random()
    if (x*x+y*y)<1:
        d=d+1
  
print(str(4*d/c))
