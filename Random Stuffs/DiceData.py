import random
import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Simulate rolling a die 1000 times
num_rolls = 100000
rolls = [random.randint(1, 10) for _ in range(num_rolls)]

# Step 2: Count frequency of each outcome
roll_counts = Counter(rolls)

# Step 3: Plot results
plt.bar(roll_counts.keys(), roll_counts.values(), color='red')
plt.xlabel("Dice Number")
plt.ylabel("Frequency")
plt.title(f"Distribution of {num_rolls} Dice Rolls")
plt.show()