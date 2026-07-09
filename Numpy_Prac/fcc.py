import numpy as np

# # a = np.array([1, 2, 3, 4, 5], dtype=np.int16)
# # print(a)

# # b = np.array([[1, 2, 3], [4, 5, 6]])
# # print(b)
# # print(a.shape)
# # print(b.shape)
# # print(a.ndim)
# # print(b.ndim)
# # print(a.dtype)
# # print(b.dtype)
# # print(a.itemsize)
# # print(b.size)
# # print(b.nbytes)


# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a)
# print(a[1,3]) # for specific element
# print(a[:,1]) # for specific column
# print(a[1,:]) # for specific rows
# print(a[0, 1:-1:2]) #variable[row, startingindex,endingindex,stepsize]
# a[1,3]=30 # if i need to change we update like this in numpy
# print(a)
# a[:,2]=[2,3] #if we need to change the whole column we change like this
# print(a)

# #example of 3d array
# b = np.array([[[1,2],[3,4]],[[5,6],[7,8],]])
# print(b)
# print(b.ndim)
# print(b[0,1,1])
# print(b[:,:,1])#it prints column 2
# print(b[:,1,:])#it prints row 2
# b[:,0,:]=[[9,9],[8,8]]
# print(b)

# #intializing diffrent types of array
# print(np.zeros((2,2,2)))
# print(np.ones((2,2,2)))
# print(np.full_like(a,2))
# print(np.full(a.shape,3))
# print(np.random.rand(2,4))
# print(np.random.random_sample(a.shape)) # for random decimals values
# print(np.random.randint(100,110, size=(3,3))) # for random int
# print(np.identity(3))
# arr = np.array([[1,2,3]])
# r1= np.repeat(arr, 3, axis=0)
# print(r1)
# output = np.ones([5,5])
# print(output)
# r2 = np.zeros((3,3))
# r2[1,1] = 9
# print(r2)
# output[1:4,1:4] = r2
# print(output)


# a = np.zeros((6, 6))

# b = np.ones((2, 2)) * 7

# a[2:4, 3:5] = b

# print(b)

# a = np.array([1,2,3])
# b = a
# b = a.copy() #we can write like this as well instead of b =a
# b [0] = 100
# print(b)


# #Mathematics

# arr = np.array([10, 20, 30, 40, 50])

# print(arr.sum())

# print(arr.mean())

# print(arr.max())

# print(arr.min())

# print(arr.argmax())

# print(arr.argmin())

# print(np.cos(arr))
# print(np.sin(arr))
# print(np.tan(arr))

# # Linear Algebra
# a = np.ones((2,3))
# b = np.full((3,2), 2)
# print(a)
# print(b)
# print(np.matmul(a,b))

marks = np.array([30,79,98,70,81])
print(marks > 80)
print(marks[marks>80])
results = np.where(
    marks > 40,
    'pass',
    'fail'
)
print(results)

arr = np.array([1,2,3,4,5])
print(np.where(arr % 2 ==0,100,0))
