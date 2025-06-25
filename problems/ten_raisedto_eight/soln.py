"""
PROBLEM

Print numbers from 0 - 10**8 in less then 30 secs. It can be printed anywhere - in the console, or even in the file.
"""

import time
import numpy as np

start_time = time.time()

arr = np.arange(100_000_000, dtype=np.int32)
np.save("nums.npy", arr)

arr = np.load("nums.npy")

with open("nums.txt", "w") as f:
    batch_size = 1_000_000
    for i in range(0, len(arr), batch_size):
        batch = arr[i:i+batch_size]
        f.write(",".join(map(str, batch)) + ",")

end_time = time.time()

print(f"Time: {end_time - start_time}")