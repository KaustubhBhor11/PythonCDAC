# list1=[1,2,3,4,5]
# list2=[7,1,7,0,2]




# # Add two list
# addedList=[]
# if len(list1) == len(list2):
#     for i in range(len(list1)):
#         addedList.append(list1[i]+list2[i])
#     print(list1)
#     print(list2)
#     print(addedList)
# else:
#     print("List length does not match")

# # check to see if two lists are equal
# if len(list1) == len(list2):
#     for i in list1:
#         if i not in list2:
#             print("list are not equal")
# else:
#     print("list are not equal")


# remove dublicated from list
# elements=[90,7,90,56,33,89,90,12,67]
# no_duplicate=[]
# for i in elements:
#     if i not in no_duplicate:
#         no_duplicate.append(i)
# print(no_duplicate)


# #Check if lists are equal
# l1=["10",20,30]
# l2=[20,"10",30]
# flag=True
# for i in l1:
#     if i in l2:
#         continue
#     else:
#         flag=False
#         break
# if (flag==False):
#     print("list not EQUAL")
# else:
#     print("list equal")



# # create list of all odd number from 1 to 100
# list=[i for i in range(1,100) if i%2!=0]
# print(list)

# # create list of all Prime number from 1 to 100
def isPrime( i ):
    for r in range(2,int(i/2)):
        if i%r == 0:
            return False
    return  True

# primelist=[i for i in range(2,100) if isPrime(i)]  
# print(primelist)


#Swap first and last elemebnt to list
# a=[89,90,45,78,34]
# a[0],a[-1]=a[-1],a[0]
# print(a)

# Create list from 1 to 100 , divide list into  even odd and prime
even=[]
odd=[1]
prime=[2]
for i in range(2,101):
    if i%2==0 :
        even.append(i)
    else:
        odd.append(i)
        if isPrime(i):
            prime.append(i)

print(tuple(even))
print(tuple(odd))
print(tuple(prime))
