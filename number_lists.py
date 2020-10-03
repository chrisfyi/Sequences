empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for number_list in numbers:  # number_list is bound to even numbers
    print(number_list)

    for value in number_list:  # value is bound to odd numbers
        print(value)