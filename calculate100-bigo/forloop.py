import time
time.time()

timstamp1 = time.time()

# Program to find Sum of N natural numbers

number = 100
total = 0

for value in range(1, number + 1):
    total += value

print("The sum is", total)

# Program completed

timestamp2 = time.time()
print("Time taken by the program is", timestamp2 - timstamp1, "seconds")