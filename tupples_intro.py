# you can tell its a tuple because it prints in () instead of []
# Tuples are immutable "Cant be changed"
# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]
print(len(albums))  # tuple contains 5 albums with 3 items
# Its good to use a tuple when you want to have ints and str or "heterogeneous"

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

# or
print()
for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

# print(metallica)
#
# print(metallica[0])  # Album name
# print(metallica[1])  # Artist
# print(metallica[2])  # Year

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# name, length, width, height, price = table
# print(length * width)

#
# # metallica[0] = "Master of Puppets" #  Will get an error
# metallica2 = list(metallica)
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)
