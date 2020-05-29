# Christian Nelson
# 5/27/2020
# DATA-51100-002, SUMMER 2020
# PROGRAMMING ASSIGNMENT #3 Nearest Neighbor

# Import numPy
import numpy as np

# Formats
fm1 = "Accuracy: {x:.2f}%"
fm2 = "{},{},{}"

# Initialize variables
correct = 0
arr_positions = np.arange(75)


# Load in iris-training-data.csv into 2 ndarrays we use usecols, and dtype to sepertate the correct data into sepertate arrays of one type
training_attribute_array = np.loadtxt('iris-training-data.csv', dtype=float, delimiter=',',usecols=(0,1,2,3))
training_class_lables_array = np.loadtxt('iris-training-data.csv', dtype=str, delimiter=',',usecols=(4))

# Load in iris-testing-data.csv into 2 ndarrays
testing_attribute_array = np.loadtxt('iris-testing-data.csv', dtype=float, delimiter=',',usecols=(0,1,2,3))
testing_class_lables_array = np.loadtxt('iris-testing-data.csv', dtype=str, delimiter=',',usecols=(4))

# Algorithm for computing distance of 2 pairs
def compute_distance(x,y):
    # compute distance = (((slx-sly)**2)+((swx-swy)**2)+((plx-ply)**2)+((pwx-pwy)**2))**0.5  for the specified position in the arrays
    distance = (((training_attribute_array[x,0]-testing_attribute_array[y,0])**2)+
((training_attribute_array[x,1]-testing_attribute_array[y,1])**2)+
((training_attribute_array[x,2]-testing_attribute_array[y,2])**2)+
((training_attribute_array[x,3]-testing_attribute_array[y,3])**2))**0.5
    #Tester code to delete
    #print(x,distance)
    return distance

# Vectorize over each distance
distances = np.vectorize(compute_distance)

# Print Results to Screen
print("DATA-51100-002, SUMMER 2020")
print("Christian Nelson")
print("PROGRAMMING ASSIGNMENT #3\n")
print("#, True, Predicted")

# Print each of our pairs
for x in range(0, 75):
    # Get the closest distance index for each pair
    closest_distance = np.argmin(distances(arr_positions,x))
    # Print the results
    if closest_distance in range(0,24):
        print(fm2.format((x+1),training_class_lables_array[x],"Iris-setosa"))
        if(testing_class_lables_array[x] == 'Iris-setosa'):
            correct += 1
    elif closest_distance in range(25,49):
        print(fm2.format((x+1),training_class_lables_array[x],"Iris-versicolor"))
        if(testing_class_lables_array[x] == 'Iris-versicolor'):
            correct += 1
    elif closest_distance in range(50,74):
        print(fm2.format((x+1),training_class_lables_array[x],"Iris-virginica"))
        if(testing_class_lables_array[x] == 'Iris-virginica'):
            correct += 1

# Get accuracy            
accuracy = float(correct/75.0)
accuracy_precentage = (accuracy * 100.0)

# Print Accuracy to screen
print(fm1.format(x=accuracy_precentage))