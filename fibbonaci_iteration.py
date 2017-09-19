# Method that generates nth fibonacci number iteratively.
def fibonacci(n):
    now = 0
    previous = 0
    temp = 0    
    for i in range(n):
        if now == 0 and previous == 0:
            now = 1 
        else:
            temp = now
            now = now + previous
            previous = temp 
    return now



