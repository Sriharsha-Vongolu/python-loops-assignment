##### Task 1: Create an Array and Basic Math ###

import numpy as np
import time

temps_celsius = np.array([22,25,28,24,26])
temps_fahrenheit = (temps_celsius * 1.8) + 32
average_fahrenheit = np.average(temps_fahrenheit)

print(temps_celsius)
print(temps_fahrenheit)
print(average_fahrenheit)

#### Task 2: Array Shape and Statistics ######
arr = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print(np.shape(arr))
print(np.size(arr))
print(np.max(arr))
print(np.min(arr))
print(np.max(arr) - np.min(arr))


###### Task 3: Performance Comparison #####
numpy_array = np.arange(1, 50001)
python_list = list(range(1, 50001))

#NumPy Sum
start_time = time.time()
numpy_sum = np.sum(numpy_array)
numpy_time = time.time() - start_time

#Pythom List sum
start_time = time.time()
python_sum = sum(python_list)
python_time = time.time() - start_time


if numpy_sum != python_sum:
    print("Error: Sums do not match")
else:
    print("NumPy Sum:", numpy_sum)
    print("Python sum:", python_sum)

print(f"NumPy Time: {numpy_time:.4f} seconds")
print(f"Python time: {python_time:.4f} seconds")

if numpy_time > 0 :
    ratio = python_time / numpy_time
    print(f"NumPy is {ratio:.1f}x faster")
else:
    print("Numpy time is too small to caluclate ratio")

