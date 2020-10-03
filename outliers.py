data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185,
        187, 188, 191, 350, 360]

                        # TESTS
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185,
#         187, 188, 191]

# data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185,
#         187, 188, 191, 350, 360]

# data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185,
#         187, 188, 191]

# data = [4, 5, 350, 360]

# data = []


# del data[0:2] # deleting 4, 5
# print(data)
#
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# lines 14 - 17 will not work
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
# print(data)

# this will only work with data that's sorted
# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop) # for debugging
del data[:stop]  # delete the data after the loop terminates(break)
print(data)

# now we're going to process the high vaules in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    # print(index)
    if data[index] <= max_valid:
        # we have the index of the last item to keep
        # set 'start' to the position of the first
        # item to delete, which is 1 after 'index'
        start = index + 1
        break
print(start)  # for debugging
del data[start:]  # everything from the start value[13] to the end
print(data)

# lines 32 - 39 identifies the first item to delete. It sets start to
# the position to start deleting from, instead of the position of the last
# item we want to keep
