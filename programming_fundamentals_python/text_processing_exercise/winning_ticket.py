tickets = input().split(", ")
winning_symbols = ['@', '#', '$', '^']
for ticket in tickets:
    ticket = ticket.strip()
    valid = False
    winning = False
    if len(ticket) == 20:
        valid = True
        middle = int(len(ticket) / 2)
        first_half = ticket[:middle]
        second_half = ticket[middle:]
        for symbol in winning_symbols:
            for repetitions in range(10, 5, -1):
                if symbol * repetitions in first_half and symbol * repetitions in second_half:
                    winning = True
                    if repetitions == 10:
                        print(f"ticket \"{ticket}\" - 10{symbol} Jackpot!")
                        break
                    else:
                        print(f"ticket \"{ticket}\" - {repetitions}{symbol}")
                        break
    if not valid:
        print("invalid ticket")
    if valid and not winning:
        print(f"ticket \"{ticket}\" - no match")
