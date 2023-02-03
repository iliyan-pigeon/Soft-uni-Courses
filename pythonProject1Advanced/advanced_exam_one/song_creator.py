def add_songs(*songs):
    songs_dict = {}
    result = ''

    for song in songs:
        song_title = f"- {song[0]}"
        song_content = song[1]
        if song_title not in songs_dict:
            songs_dict[song_title] = []
        for line in song_content:
            songs_dict[song_title].append(line)

    for key, value in songs_dict.items():
        result += f"{key}\n"
        for line in value:
            result += f"{line}\n"

    return result


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))