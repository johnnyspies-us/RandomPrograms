import random
import matplotlib.pyplot as plt
from collections import Counter

rolls = 100
random_num = [random.randrange(1,100) for _ in range(rolls)]

num_counts = Counter(random_num)

print(num_counts)

plt.bar(num_counts.keys(), num_counts.values(), color="blue")
plt.xlabel("Numbers")
plt.ylabel("Amount of Occurinces")
plt.show()
