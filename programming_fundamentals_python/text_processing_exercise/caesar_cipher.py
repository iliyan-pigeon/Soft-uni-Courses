sentence = input()
encrypted_sentence = ''
for ch in sentence:
    encrypted_sentence += chr(ord(ch) + 3)
print(encrypted_sentence)
