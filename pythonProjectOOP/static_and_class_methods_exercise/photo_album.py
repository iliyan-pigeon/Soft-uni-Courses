from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for p in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):
        for page in range(self.pages):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        result = "-----------"
        for page in self.photos:
            result += f"\n{('[] ' * len(page)).rstrip()}"
            result += "\n-----------"

        return result


