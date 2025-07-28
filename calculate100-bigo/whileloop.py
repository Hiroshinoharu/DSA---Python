import time
time.time()

timstamp1 = time.time()

# Program to find Sum of N natural numbers

number = 100

if number < 0:
    print("Please enter a positive integer.")
else:
    sum = 0
    # Use a while loop to iterate until 0
    while (number > 0):
        sum = sum + number
        number -= 1

print("The sum is", sum)

# Program completed

timestamp2 = time.time()
print("Time taken by the program is", timestamp2 - timstamp1, "seconds")