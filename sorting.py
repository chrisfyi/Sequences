pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)
# uppercase sorts before lowercase unless you use casefold method
# sorted returns a list containing all items of an iterable
# sorted returns a new list, .sort does not.
numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print()
# you shouldn't assign a new variable to .sort, it'll return none
another_sorted_numbers = numbers.sort()
print(another_sorted_numbers)

print()

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)
