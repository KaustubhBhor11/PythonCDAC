# Assignment 1
from functools import reduce


def elements_greater_than_n(list1: list, n: int) -> list:
    x = [i for i in list1 if i > n]
    return x


# Assignment 2
def square_list(list1: list) -> list:
    x = [i * i for i in list1]
    return x


# map function
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(elements_greater_than_n(list1, 5))
print(square_list(list1))
map(lambda x: x ** 2, list1)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(list(map(lambda x, y: x * y, list1, list2)))


# filter function
def greater_than_10(n):
    if n > 10:
        return True
    else:
        return False


cv = list(filter(greater_than_10, list2))
print(cv)

# reduce function
x = reduce(lambda s, d: s + d, list2)
print(x)

a=[1,5,7,9,11,9]
b=[7,5,1,2,8]
def get_same_elements(a,b):
    same=[]
    for i in b:
        if i in a:
            same.append(i)
    return same

#Get all common elements from 2 lists
def get_same_element(a,b=b): #Approach 1
    if a in b:
        return True
    else:
        return False
sd=list(filter(get_same_element,a))
print(sd)

print(list(filter(lambda x: x in a,b))) #Approach 2: better one as no need to add default parameter



#Question : s="Hello world. How are you ?" result= [HELLO,hello,5], [WORLD,world,5] ,[HOW,how,3], [ARE,are,3], [YOU,you,3]

