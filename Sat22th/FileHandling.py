# f=open("test.txt","w")
# f.write("File is created")
# f.close()
# x=open("test.txt","r")
# test_file_data=x.read()
# x.close()
# print(test_file_data)
#
from os.path import split


# function to copy the file

# def copy_file(path):
#     try:
#         file1 = open(path, "r")
#         file1_data = file1.read()
#         new_file_name = path.split(".")[0] + "_copy." + path.split(".")[-1]
#         file2 = open(new_file_name, "w")
#         file2.write(file1_data)
#         file2.close()
#     except:
#         print("please enter valid file path")
#     else:
#         print("file is copied")
#
#
# copy_file("test.txt")

# Capitalize all the words in file
# def capitalise_words(string):
#     words = string.split()
#     capitalised = [word.capitalize() for word in words]
#     result = " ".join(capitalised)
#     return result
#
#
# def capitalize_data(path):
#     try:
#         with open(path, "r") as f:
#             f1_data = f.read()
#             f.close()
#         with open(path, "w") as f:
#             data = capitalise_words(f1_data)
#             f.write(data)
#             f.close()
#     except:
#         print("please enter valid file path")
#
#
# capitalize_data("test.txt")


# Count the number of words in file
# import re
#
#
# def count_words(string):
#     words = re.findall("[a-zA-Z0-9]+", string)
#     return words
#
#
# def count_words_in_file(path):
#     with open(path, "r+") as f:
#         file_data = f.read()
#         f.close()
#         words_list = count_words(file_data)
#         return len(words_list)
#
#
# print(count_words_in_file("test.txt"))


# writing objects to the file
# class Student:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#     def __repr__(self):
#         return f"Student id :{self.id} Student Name :{self.name}"
#
#
# s1 = Student(1, "Ram")
#
#
# def write_obj_to_file(path, obj):
#     with open(path, "r+") as f:
#         f.write(str(obj))
#         f.close()


# write_obj_to_file("test.txt", s1)

def count_char(string):
    alphanum = []
    spaces = []
    special_char = []
    for i in string:
        if i.isalnum():
            alphanum.append(i)
        elif i == " ":
            spaces.append(i)
        else:
            special_char.append(i)
    counts = {"alphanum": len(alphanum), "spaces": len(spaces), "special_char": len(special_char)}

    return counts


def count_char_in_file(path):
    with open(path, "r+") as f:
        file_data = f.read()
        f.close()
    return count_char(file_data)
