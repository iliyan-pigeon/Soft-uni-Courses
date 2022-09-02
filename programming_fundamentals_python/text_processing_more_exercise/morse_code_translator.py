morse_code_dict = {'.-': 'A', '-...': 'B',
                    '-.-.': 'C', '-..': 'D', '.': 'E',
                    '..-.': 'F', '--.': 'G', '....': 'H',
                    '..': 'I', '.---': 'J', '-.-': 'K',
                    '.-..': 'L', '--': 'M', '-.': 'N',
                    '---': 'O', '.--.': 'P', '--.-': 'Q',
                    '.-.': 'R', '...': 'S', '-': 'T',
                    '..-': 'U', '...-': 'V', '.--': 'W',
                    '-..-': 'X', '-.--': 'Y', '--..': 'Z'}
final_message = ''
encrypted_words = input().split(" | ")
for word in encrypted_words:
    letters = word.split()
    final_word = ''
    for letter in letters:
        final_word += morse_code_dict[letter]
    final_message += final_word + " "
print(final_message)
