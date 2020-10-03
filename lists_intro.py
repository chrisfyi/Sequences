computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

# computer_parts[3] = "trackball" # changes the string at index position 3
print(computer_parts[3:])
computer_parts[3:] = ["trackball"]  # using a slice to replace mouse and mat
print(computer_parts)

# for part in computer_parts:
#     print(part)
#
# print()
# print(computer_parts[2])
#
# print(computer_parts[0:3])
# print(computer_parts[-1])