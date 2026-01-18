import numpy as np
rand_fun=np.random.rand(2,3)
rand_arr=np.random.randn(3,3)
rand_array_int=np.random.randint(1,10,size=(5,5))
print("Rand_Function: ",rand_fun)
print("\n")
print("Normal Random Number Array: ",rand_arr)
print("\n")
print("Random Array: ",rand_array_int)



"""""
NumPy provides functions to create arrays filled with random numbers.

np.random.rand(): Creates an array of specified shape and fills it with random values sampled from a uniform distribution over [0, 1).
np.random.randn(): Creates an array of specified shape and fills it with random values sampled from a standard normal distribution.
np.random.randint(): Creates an array of specified shape and fills it with random integers within a given range.
"""