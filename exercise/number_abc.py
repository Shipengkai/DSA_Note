import time


start = time.time()
for a in range(1001):
    for b in range(1001):
        if a**2 + b**2 == (1000-a-b)**2:
            print(f"a: {a}, b: {b}, c: {1000-a-b}")
end = time.time()
print(end-start)
