class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, millilitres):
        if self.content + millilitres <= Glass.capacity:
            self.content += millilitres
            return f"Glass filled with {millilitres} ml"
        return f"Cannot add {millilitres} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        space_left = Glass.capacity - self.content
        return f"{space_left} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())