from Tue18th import functions

if __name__ == "__main__":
    print(functions.add(5, 8))
    print(functions.is_prime(71))

    list1 = {i for i in range(100) if i % 2 == 0}
    print(list1)

    print(functions.convert_identifier_case("the_new_class"))


