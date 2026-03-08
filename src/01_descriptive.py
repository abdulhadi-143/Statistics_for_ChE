"""
01_descriptive.py
=================
Descriptive Statistics — implemented from scratch.

Source  : IIT Madras — Statistics for Experimentalists
Lecturer: Dr. A. Kannan, Chemical Engineering Department
Author  : Abdul Hadi, Mersin University
"""
"""The formula for the mean is Mean=Sum of the sample data)/number of time it have taken"""
import numpy as np

def sample_mean(data:list):
    #calculate the mean of the given sample
    n=len(data)
    total=sum(data)
    return total/n

#test
yields = [72, 74, 65, 67, 70]
my_mean=sample_mean(yields)
numpy_mean=np.mean(yields)
print(f"My mean: {my_mean}")
print(f"Numpy mean: {numpy_mean}")



"""Now we will see another important function in statistics that is VARIANCE and formula for the variance is s² = Σ(xᵢ - x̄)² / (n - 1)
So lets try to prove our results by matching the results shown by using numpy std function"""

def sample_variance(data:list):
    #calculated the variance of the given sample.
    n = len(data)
    mean = sample_mean(data)
    sum_of_squares = 0
    for x in data:
        diff = x - mean
        squared = diff ** 2
        sum_of_squares = sum_of_squares + squared
    return sum_of_squares / (n - 1)

import numpy as np

numpy_variance=np.var(yields, ddof=1)

print(f"My variance: {sample_variance(yields)}") 
print(f"Numpy variance: {numpy_variance}")



"The procedure for the standard deviation is to take the square root of the variance and the formula is s = sqrt(s²) where s² is the variance"
import math
def sample_std(data: list):
    return math.sqrt(sample_variance(data))  #or return sample_variance(data) ** 0.5

print(f"My std dev    : {sample_std(yields)}")
print(f"Numpy std dev : {np.std(yields, ddof=1)}")