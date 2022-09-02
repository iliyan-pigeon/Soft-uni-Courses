cards = input().split()
shuffles = int(input())
for shuffle in range(shuffles):
    middle_index = int(len(cards) / 2)
    left_side = cards[:middle_index]
    right_side = cards[middle_index:]
    current_deck = []
    for card in range(len(left_side)):
        current_deck.append(left_side[card])
        current_deck.append(right_side[card])
    cards = current_deck
print(cards)
