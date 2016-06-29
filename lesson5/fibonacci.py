import time

def fibonacci(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)

start=time.time()
print(fibonacci(35))
end=time.time()
print("Calculation took", end-start, "seconds")
