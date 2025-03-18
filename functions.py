# print hello world
def hello() -> None:
    print("hello world")


hello()


# Factorial of a number
def factorial(n) -> int:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


print(factorial(5))


def is_prime(n) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(10))


def is_odd_even(n) -> None:
    if n % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')


is_odd_even(12)


# Variable argument function - similar to ... in Java
def add(*a) -> int:
    ans = 0
    for i in a:
        ans += i
    return ans


print(add(1, 5, 2, 7, 1, 8, 2, 6, 1, 9))


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

