from nested_data import albums

SONGS_LIST_INDEX = 3  # a constant is represented by all caps
SONGS_TITLE_INDEX = 1  # this is grabbing the tuples from albums

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
        # choice - 1 is because indexing starts at 0
    else:
        break

    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONGS_TITLE_INDEX]
        print("Now Playing: {}".format(title))

    print("=" * 40)
