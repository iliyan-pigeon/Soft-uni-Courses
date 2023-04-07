class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = []
        for s in songs:
            self.songs.append(s)
        self.published = False

    def add_song(self, song):
        if song not in self.songs:
            if song.single:
                return f"Cannot add {song.name}. It's a single"
            if self.published:
                return "Cannot add songs. Album is published."
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        return "Song is already in the album."

    def remove_song(self, song_name):
        for s in self.songs:
            if s.name == song_name:
                if self.published:
                    return "Cannot remove songs. Album is published."
                self.songs.remove(s)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        result = f"Album {self.name}\n"
        for s in self.songs:
            result += f"== {s.get_info()}\n"
        return result


