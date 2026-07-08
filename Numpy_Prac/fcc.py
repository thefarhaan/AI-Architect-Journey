import numpy as np

# a = np.array([1, 2, 3, 4, 5], dtype=np.int16)
# print(a)

# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)
# print(a.shape)
# print(b.shape)
# print(a.ndim)
# print(b.ndim)
# print(a.dtype)
# print(b.dtype)
# print(a.itemsize)
# print(b.size)
# print(b.nbytes)


a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
print(a[1,3]) # for specific element
print(a[:,1]) # for specific column
print(a[1,:]) # for specific rows
print(a[0, 1:-1:2]) #variable[row, startingindex,endingindex,stepsize]
a[1,3]=30 # if i need to change we update like this in numpy
print(a)
a[:,2]=[2,3] #if we need to change the whole column we change like this
print(a)
#example of 3d array
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print(b.ndim)
print(b[0,1,1])
print(b[:,:,1])#it prints column 2
print(b[:,1,:])#it prints row 2
b[:,1,:]=[[9,9],[8,8]]
print(b)
