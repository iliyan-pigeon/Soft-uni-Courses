def words_sorting(*args):

    def creating_dictionary(numbers):
        words_values = {}
        for word in numbers:
            word_value = sum(map(ord, list(word)))
            words_values[word] = word_value
        return words_values

    def sorting_dictionary(dictionary):
        total_dictionary_value = 0

        for key, value in dictionary.items():
            total_dictionary_value += value

        if total_dictionary_value % 2 == 0:
            ordered_dictionary = sorted(dictionary.items(), key=lambda x: x[0])
        else:
            ordered_dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
        return ordered_dictionary

    def filling_result(words_values):
        result = ""
        for word in words_values:
            result += f"{word[0]} - {word[1]}\n"
        return result

    final_words_values = filling_result(sorting_dictionary(creating_dictionary(args)))
    return final_words_values



print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))