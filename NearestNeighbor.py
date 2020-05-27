# Christian Nelson
# 5/27/2020
# DATA-51100-002, SUMMER 2020
# PROGRAMMING ASSIGNMENT #3 Nearest Neighbor

# Import numPy
import numpy as np

# Load in iris-training-data.csv into 2 ndarrays
training_attribute_array = np.loadtxt('iris-training-data.csv', dtype=float, delimiter=',',usecols=(0,1,2,3))
# We use usecols, and dtype to sepertate the correct data into sepertate arrays of one type
training_class_lables_array = np.loadtxt('iris-training-data.csv', dtype=str, delimiter=',',usecols=(4))

# Tester code to be deleted
print(training_attribute_array)
print(training_class_lables_array)