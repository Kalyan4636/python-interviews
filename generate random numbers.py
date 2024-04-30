#  Generate Random Numbers

import random

# Generate a random integer between a specified range
random_number = random.randint(1, 100)
print("Random integer between 1 and 100:", random_number)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random floating-point number between 0 and 1:", random_float)

# Generate a random floating-point number within a specified range
random_float_range = random.uniform(1.0, 10.0)
print("Random floating-point number between 1.0 and 10.0:", random_float_range)
