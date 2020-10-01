shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies", "pasta"]
print(shopping_list)
print(id(shopping_list))
print(another_list)

a = b = c = d = e = f = another_list  # this isn't a new list, it just
# adds more items to the list
print(a)
print("Adding cream")
b.append("cream")
print(c)
print(d)
print(e)
