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

