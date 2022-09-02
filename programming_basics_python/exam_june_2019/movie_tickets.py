a1 = int(input())
a2 = int(input())
n = int(input())
a2_first_symbol = a2 - 1
n_second_symbol = n - 1
n_third_symbol = int(n / 2 - 1)
for first_symbol in range(a1, a2_first_symbol + 1):
    for second_symbol in range(1, n_second_symbol + 1):
        for third_symbol in range(1, n_third_symbol + 1):
            combined_symbols = first_symbol + second_symbol + third_symbol
            if first_symbol % 2 != 0 and combined_symbols % 2 != 0:
                print(f"{chr(first_symbol)}-{second_symbol}{third_symbol}{first_symbol}")
