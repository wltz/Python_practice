import numpy as np

a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(a)

# Get a specific element [r,c]
print(a[1,2]) # 8

# Get a specific row
print(a[0, :])

# Get a specific column
print(a[:, 1])

# Get elements with certain rules [start_idx:end_idx:step]
print(a[0,0:5:2]) # [1 3 5]
print(a[0,0:-1:2]) # [1 3]
print(a[0,2:6:9]) # [3]

# change value
a[1,0] = 20
print(a)
a[0, :] = -20
print(a)

# 3D 
b = np.array([[[1,2,3], [3,4,5]], [[6,7,8],[8,9,10]]])
print(b)

# get specific num
print(b[1,1,1]) # 9
print(b[1,:, :])
print(b[0, :, 1]) # [2 4]
print(b[1, 0, :]) # [6 7 8]

# Initialize different types of arrays
c = np.zeros((3,3,3))
print(c)

c1 = np.ones((2,3,4), dtype='int32')
print(c1)

# other num
c3 = np.full((3,3,3), 9)
print(c3)

# change value of existing array
print(np.full_like(c,9))

# random num
ran =np.random.rand(4,5,6)
print(ran)

# random int
rand_int = np.random.randint(1,10, size=(5,5))
print(rand_int)

# The identity matrix
idmtx = np.identity(3)
print(idmtx)

# Copy arrays
a = np.array([9,9,9])
b = a
b[0] = 0
print(b) # [0 9 9]
print(a) # [0 9 9], a got changed

b = a.copy()
b[0] = 9
print(b) # [9 9 9]
print(a) # [0 9 9] ,stay unchanged.

####### Linear Algebra

# Matrix multiplication
a = np.full((3,2), 3)
print(a)
b = np.ones((2,3))
print(b)
mul_ab = np.matmul(a,b)
mul_ba = np.matmul(b,a)
print(mul_ab)
print(mul_ba)


### Reorganizeing arrays
# reshape
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape) # (2, 3)
b = a.reshape((3,2))
print(b)
print(b.shape) # (3, 2)

# vertically stack
r1 = np.array([1,2,3])
r2 = np.array([4,5,6])
m1 = np.vstack([r1,r2])
print(m1)
m1 = np.vstack([m1,m1])
print(m1)

# Horizontal stack
c1 = np.array([1,1,1])
c2 = np.array([2,2,2])
m2 = np.hstack([c1,c2])
print(m2)

### Miscellaneous
# Load data from file
print("Load data from file")
data = np.genfromtxt('/harddisk1/liangzhao/Projects/pytest/data.txt', delimiter=',')
data = data.astype('int32') # convert the data type to int32
print(data)
data_copy = data[data%2 != 1]
print(data_copy)

# get the element with a list of index
data2 = np.array((1,2,3,4,5,6))
data2 = data2[[0,1,-1]]
print(data2)