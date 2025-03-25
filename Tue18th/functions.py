# print hello world
from typing import List, Any


def hello() -> None:
    print("hello world")


# Factorial of a number
def factorial(n) -> int:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def is_prime(n) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_odd_even(n) -> None:
    if n % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')


# Variable argument function - similar to ... in Java
def add(*a) -> int:
    ans = 0
    for i in a:
        ans += i
    return ans


# Lambda/Anonymous function
def add(a, b) -> int:
    return a + b


def subtract(a, b) -> int:
    return a - b


# Advantage of Lambda is: 1. Reduces code 2. Is Anonymous
add = lambda a, b: a + b
sub = lambda a, b: a - b


def convert_identifier_case(s) -> str:
    if "_" in s:
        list1 = [l.capitalize() for l in s.split("_")]
        list1 = "".join(list1)
        return list1
    else:
        s1 = ""
        for i in range(0, len(s)):
            if s[i].isupper() and i != 0:
                s1 += "_"
                s1 += s[i].lower()
            else:
                s1 += s[i].lower()
        return s1


# prime numbers for range 10-20 30-40 in 1 list
def is_prime_odd():
    prime_list = []
    for i in range(2, 41):
        # print(i)
        if (9 < i and i < 21) or (29 < i and i < 41):
            if is_prime(i):
                prime_list.append(i)
    return prime_list


# recursion to find factorial
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


# List comprehension
x = [i for i in range(0, 11) if is_prime(i)]

list_of_input = [10, 12, 68, 3, 2, 7, 9, 11, 56, 43, 67]
even = [i for i in list_of_input if (i % 2 == 0)]
odd = [i for i in list_of_input if (i % 2 != 0)]
prime = [i for i in list_of_input if is_prime(i)]

list_of_names = ["ajay", "pratik", "asam"]
t = [i for i in list_of_names if i[0] == "a"]

# number of vovels should me more then one
vowel = ["a", "e", "i", "o"]


# make list of strings that have 1 or more vowels
def count_vowels(s):
    count = 0
    for i in s:
        if i in vowel:
            count += 1
    return count


c = [i for i in list_of_names if count_vowels(i.lower()) > 2]

# assignment
# make list of strings that have 1 or more consonents
input_String = "this is fun"
s = ""


def encode_string(s: str) -> str:
    final_string = ""
    for i in s:
        if (i not in vowel) and (i != " "):
            final_string += i + "o" + i
        else:
            final_string += i
    return final_string


# Assignment 2
def string_greater_than_n(l: list, n: int) -> list:
    result = [i for i in l if len(i) > n]
    return result


# iterator
iterator = iter(list_of_input)
print(next(iterator))


print(list_of_input)
print(sorted(list_of_input))
print(list_of_input)
print([x for x in reversed(list_of_input)])
print(list_of_input)

