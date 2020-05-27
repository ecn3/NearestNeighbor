# Christian Nelson
# 5/27/2020
# DATA-51100-002, SUMMER 2020
# PROGRAMMING ASSIGNMENT #3 Nearest Neighbor

# Import numPy
import numpy as np

# Load in iris-training-data.csv into 2 ndarrays we use usecols, and dtype to sepertate the correct data into sepertate arrays of one type
training_attribute_array = np.loadtxt('iris-training-data.csv', dtype=float, delimiter=',',usecols=(0,1,2,3))
training_class_lables_array = np.loadtxt('iris-training-data.csv', dtype=str, delimiter=',',usecols=(4))

# Load in iris-testing-data.csv into 2 ndarrays
testing_attribute_array = np.loadtxt('iris-testing-data.csv', dtype=float, delimiter=',',usecols=(0,1,2,3))
testing_class_lables_array = np.loadtxt('iris-testing-data.csv', dtype=str, delimiter=',',usecols=(4))

'''
# Tester code to be deleted
print("training_attribute_array",training_attribute_array)
print("training_class_lables_array",training_class_lables_array)
print("testing_attribute_array",testing_attribute_array)
print("testing_class_lables_array",testing_class_lables_array)
'''

# Algorithm for computing distance of 2 pairs
def compute_distance(slx,swx,plx,pwx,sly,swy,ply,pwy):
    distance = (((slx-sly)**2)+((swx-swy)**2)+((plx-ply)**2)+((pwx-pwy)**2))**0.5 
    # Tester code to be deleted
    #print(distance)

# Print Results to Screen
print("DATA-51100-002, SUMMER 2020")
print("Christian Nelson")
print("PROGRAMMING ASSIGNMENT #3\n")


'''
# Tester code to be deleted
compute_distance(training_attribute_array[0,0],training_attribute_array[0,1],training_attribute_array[0,2],
training_attribute_array[0,3],testing_attribute_array[0,0],testing_attribute_array[0,1],
testing_attribute_array[0,2],testing_attribute_array[0,3]
)

'''