import numpy as np

array1 = np.array([1, 2, 34, 5, 6, 77, 8], dtype="int32")

array2 = np.array([6, 89, 4, 8, 12, 42, 9])
print(type(array1[0]))
print(array1 ** 2)
print(array1 + array2)
print(array1 - array2)
print(array1 / array2)

array1.sort()
array3 = np.concat([array2, array1])
print("np.concat([array2,array1])", array3)

deep_copy = array3.copy()
shallow_copy = array3.view()
print("deep_copy", deep_copy)
print("shallow_copy", shallow_copy)

# numpy arrays of strings and artimatic operations
# commented operations are not vaid
string_array1 = np.array(["ram", "sham", "tom"])
string_array2 = np.array(["nam", "hare", "jerry"])
print("\n", "numpy arrays of strings and artimatic operations", "\n")
print(type(string_array1[0]))
# print(string_array1*2)
# print(string_array1-2)
# print(string_array1+2)
# print(string_array1/2)
print("string_array1+string_array2", string_array1 + string_array2)
# print("string_array1-string_array2",string_array1-string_array2)
# print("string_array1/string_array2",string_array1/string_array2)

# split array in n parts
print(np.array_split(array1, 3))

from numpy import random

rand_numb = random.randint(100, 500, 10)
print(rand_numb)
rand_numb1 = random.choice([1, 2, 3, 4, 54, 5, 6, 7, 8, 8], 2)
print(rand_numb1)
print(array1)
random.shuffle(array1)
print("random.shuffle(array1)", array1)

zeros=np.zeros(10)
onces=np.ones(10)

zeros1=np.concat([zeros ,[1,2,3,4]])
zeros1=zeros1.astype(int)
print(zeros1)

print(np.count_nonzero (zeros1))


