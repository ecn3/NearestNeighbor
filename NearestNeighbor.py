# Christian Nelson
# 5/27/2020
# DATA-51100-002, SUMMER 2020
# PROGRAMMING ASSIGNMENT #3 Nearest Neighbor

# Import numPy
import numpy as np

# Formats
fm1 = "Accuracy: {x:.2f}%"
fm2 = "{},{},{}"

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
def compute_distance(x,y):
    # compute distance = (((slx-sly)**2)+((swx-swy)**2)+((plx-ply)**2)+((pwx-pwy)**2))**0.5  for the specified position in the arrays
    distance = (((training_attribute_array[x,0]-testing_attribute_array[y,0])**2)+
((training_attribute_array[x,1]-testing_attribute_array[y,1])**2)+
((training_attribute_array[x,2]-testing_attribute_array[y,2])**2)+
((training_attribute_array[x,3]-testing_attribute_array[y,3])**2))**0.5
    # Tester code to be deleted
    #print(distance)
    return distance


# Print Results to Screen
print("DATA-51100-002, SUMMER 2020")
print("Christian Nelson")
print("PROGRAMMING ASSIGNMENT #3\n")
print("#, True, Predicted")

correct = 0

for y in range(0, 75):
    closest_dist = 100
    position = 0
    for x in range(0, 75):
        distance = compute_distance(x,y)
        if distance < closest_dist:
            closest_dist = distance
            position = x
    if position in range(0,24):
        print(fm2.format((y+1),training_class_lables_array[y],"Iris-setosa"))
        if(testing_class_lables_array[y] == 'Iris-setosa'):
            correct += 1
    elif position in range(25,49):
        print(fm2.format((y+1),training_class_lables_array[y],"Iris-versicolor"))
        if(testing_class_lables_array[y] == 'Iris-versicolor'):
            correct += 1
    elif position in range(50,74):
        print(fm2.format((y+1),training_class_lables_array[y],"Iris-virginica"))
        if(testing_class_lables_array[y] == 'Iris-virginica'):
            correct += 1

accuracy = float(correct/75.0)
accuracy_precentage = (accuracy * 100.0)

print(fm1.format(x=accuracy_precentage))