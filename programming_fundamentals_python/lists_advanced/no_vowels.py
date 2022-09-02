vowels = ['a', 'o', 'u', 'e', 'i']
word = [ch for ch in input() if ch.lower() not in vowels]
print("".join(word))

