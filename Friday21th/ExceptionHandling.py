# a = 10
# b = 0
# try:
#     c = a // b
#
# except ZeroDivisionError as e:
#     print("no not use zero")
#     print(e)
# else:
#     print(c)
# finally:
#     print("i will always work")
#
#
# # Arithmatic exception handling
# def divide(n1: int, n2: int):
#     try:
#         c = n1 / n2
#     except:
#         print("Please enter non zero denominator")
#
#
# # check number exception handling
# def number_format(s: str):
#     try:
#         int(s)
#     except:
#         print("number is not valid")
#     else:
#         print("number is valid")
#
#
# # number_format("5a")
#
#
# # Access element in array exception handling
# def index_out_of_bound(list, index):
#     try:
#         print(list[index])
#     except:
#         print("index_out_of_bound")
#     else:
#         print("Process ran successfully")


# custom error
class MyCustomException(Exception):
    def __init__(self,msg="Something went Wrong"):
        self.msg=msg

a=9
try:
    if a<10:
        raise MyCustomException("Number less than 10")
    else:
        print("ok")
except MyCustomException as e:
    print(e)
