sequence = input().upper()
unique_symbols = []
final_sequence = ''
current_sequence = ''
number = ''
for ch in range(len(sequence)):
    if not sequence[ch].isnumeric():
        if len(number) != 0:
            final_sequence += current_sequence * int(number)
            current_sequence = ''
            number = ''
        if sequence[ch] not in unique_symbols:
            unique_symbols.append(sequence[ch])
        current_sequence += sequence[ch]
    elif sequence[ch].isnumeric():
        number += sequence[ch]
        if ch == len(sequence) - 1:
            final_sequence += current_sequence * int(number)
print(f"Unique symbols used: {len(unique_symbols)}")
print(final_sequence)

