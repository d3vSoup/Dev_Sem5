
import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)
print("Shape:", array_1d.shape)
print(  )

array_2d = np.array([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
])
print("2D Array:")
print(array_2d)
print("Shape:", array_2d.shape)
print("Dimensions:", array_2d.ndim)
print()
print("Dimensions:", array_1d.ndim)

print()
print("Size:", array_1d.size)
print("Size:", array_2d.size)
print()


# ndim for diemnsions ( 2 for 2D and 1 for 1D )
# shape for n x m way of saying
# size for total elements 

# print the elements of 2D array 
# -1 prints the last element

print(array_2d[0, -1])
print(array_2d[-1, -1])
print(array_2d[0, -2])

print()


#print elements of 1D

print(array_1d[0])
print(array_1d[-1])
print(array_1d[-2])

#slicing 
print()

#array slicing 
print(array_1d[0:3])
print(array_1d[2:])
print(array_1d[:3])
#print alternate elements 
print(array_1d[::2]) # jump of 2
print(array_1d[::]) # jump of 1 (Default)
print(array_1d[0:5:3]) # from index 0 to 5 with gap fo 3 each
print()


#2D 2 arrays and find the sum of all elements of 2x2 array

array_2d_1 = np.array([[1, 2], [3, 4]])
array_2d_2 = np.array([[5, 6], [7, 8]])

print("Array 1:")
print(array_2d_1)
print("Array 2:")
print(array_2d_2)

print()

#sum of all elements of 2x2 array
print("Sum of all elements of 2x2 array:")
print(array_2d_1 + array_2d_2)

# to add elements of one array ... its simply .. loop and add or sum()
print(np.array( [1,2,3]).sum()) 
print(np.array([1,2,3]).sum() + np.array([4,5,6]).sum())

#add elements of 2 1D arrays
print(array_2d_1 + array_2d_2 )

#take a 1D array and fine the total and max and min element and mean median mode
print()
array_1d = np.array([1, 2, 3, 4, 5])
print(array_1d.sum())
print(array_1d.max())
print(array_1d.min())
print(array_1d.mean())
#print(array_1d.median())
print(np.median(array_1d))
#print(array_1d.mode())
#mode needs scipy
from scipy import stats
print(stats.mode(array_1d)[0])


# now we filtr array elements 
# so lets do 2 kinds ... one... if the element > 40 and result 2 is ... element %2 == 0 

print()
arr11= np.array([10,20,36,67,89,70,3,2,56])
result1= arr11 [ arr11>40]
result2= arr11[arr11%2==0]
print(result1)
print(result2)
result3= arr11 [ (arr11>40) & (arr11%2==0)]
print(result3)



