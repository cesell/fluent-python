#%% [markdown]
# # Numpy 
#
# Operations on arrays are up to two orders of magnitude faster with numpy

#%% Imports
import numpy as np
import random
import time

#%% Creating Arrays from existing data
vector = np.array([2.5,3,5,7])
matrix = np.array([ [1,2,3], [4,5,6] ])

#%% Atributes
print(f'type vector:{vector.dtype}, dimensions vector:{matrix.ndim}, shape matrix:',
      f'{matrix.shape}, elements vector:{vector.size}, ', 
      f'element size in bytes:{vector.itemsize}')


#%% Accessing the data
for row in matrix:
    for column in row:
        print(column, end='  ')
    print()

# Access as one dimension
for i in matrix.flat:
    print(i, end=' ')
#%% Creating arrays
onevalue = np.full((3,5), 13) #3 by 5 with only 13s
a_range = np.arange(10,1,-2) #start, stop, inc
np.linspace(0.0, 1.0, num=5) #start, stop, number of points

#%% Reshaping 
vector.reshape(2,2)

#%% Performance
start = time.time()
rolls_list = [random.randrange(1,7) for i in range(0,1000000)]
end = time.time()
print(end - start)
start = time.time()
rolls_array = [np.random.randint(1,7,1000000)]
end = time.time()
print(end - start)


#%% Operations
print(vector * 2, vector * [2,2,2,2])  # same effect, broadcasting
vector += 1
print(vector)
print(vector < 4) # can use ==
print(f'suma:{matrix.sum()}, min:{matrix.min()}, mean:{matrix.mean()}')
print(f'all rows in each column:{matrix.var(axis=0)}')
print(f'sqrt: {np.sqrt(vector)}')
print(f'add: {np.add(vector, vector)}, {vector+vector}')

#%% Indexing, Slicing and Copying

print(matrix[0,1]) #row 0, column 1
print(matrix[1]) #row 1
print(matrix[:, [0,2]]) #row 0 columns 0 and 2
deep_copy = matrix.copy()  #for other objects use the deepcopy.copy function
deep_copy *= 0
print(matrix) 
print(deep_copy)  #no shared elements

#reshape returns a shallow copy, resize modifies the original
#flattens makes a hard copy, ravel a soft copy

print(matrix.T) #transpose
print(np.hstack((matrix,[[6,7],[8,9]]))) #adding additional columns, also vstack

#%%
