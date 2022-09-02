explosion_sequence = input()
final_sequence = ''
strength = 0
for ch in range(len(explosion_sequence)):
    if explosion_sequence[ch] == '>':
        final_sequence += '>'
        strength += int(explosion_sequence[ch+1])
    elif strength > 0:
        strength -= 1
    else:
        final_sequence += explosion_sequence[ch]
print(final_sequence)


