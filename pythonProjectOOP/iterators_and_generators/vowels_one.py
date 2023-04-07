from collections import deque


class vowels:
    def __init__(self, sentence):
        self.sentence = list(sentence)
        self.vowels = ["a", "e", "i", "o", "u", "y"]
        self.vowels_in_sentence = deque([ch for ch in self.sentence if ch.lower() in self.vowels])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels_in_sentence:
            raise StopIteration

        return self.vowels_in_sentence.popleft()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)