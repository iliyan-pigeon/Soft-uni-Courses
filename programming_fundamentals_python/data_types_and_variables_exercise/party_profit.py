companions_number = int(input())
days = int(input())
total_coins = 0
coins_per_companion = 0
for day in range(1, days+1):
    if day % 10 == 0:
        companions_number -= 2
    if day % 15 == 0:
        companions_number += 5
    total_coins += 50
    total_coins -= 2 * companions_number
    if day % 3 == 0:
        total_coins -= 3 * companions_number
    if day % 5 == 0:
        total_coins += 20 * companions_number
        if day % 3 == 0:
            total_coins -= 2 * companions_number
coins_per_companion = int(total_coins / companions_number)
print(f"{companions_number} companions received {coins_per_companion} coins each.")
