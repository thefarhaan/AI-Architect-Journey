import numpy as np

# Question 1
a = np.arange(0,10)
print(a)
# Question 2
print(np.reshape(a,(5,2)))
#Question 3
b = np.ones([3,3])
print(b)
#Question 4
c = b
c[1,1] = 9
print(c)
#Question 5
d = np.zeros([5,5])
print(d)
e = d
e [1:4,1:4] =5
print(e)
# Question 6
d1 = np.ones([5,5])
d2 = np.zeros([3,3])
d2[1,1] = 9
d1[1:4,1:4] = d2
print(d1)
print(d2)
# Question 7
'''
[0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]
[[0 1 2 3 4 5 6 7
  8 9 10 11 12 13 14 15]]
'''
# Question 8
'''
[0 1 2 3 4 5 6 7 8 9 10 11]
[4 5 6 7 ]
'''
# Question 9
'''
[[ 6  7]
[10 11]]
'''
# Question 10
'''
[3 7 11]
'''
#Question 11
'''
[2 12 30]
'''
# Question 12
'''
[4 16 36]
'''
# Question 13
'''
[19 18 32]
'''
#Bonus Question
bonus = np.zeros([5,5])
b1 = np.ones([3,3])
b1 [1,1] = 8
print(b1)
bonus [1:4,1:4] = b1
print(bonus)
'''
Done Where you told me to do manually use paper and pen for that and write and calculate there and write the output here
'''
