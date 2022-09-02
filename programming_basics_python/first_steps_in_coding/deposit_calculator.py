deposited_amount = float(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input())
final_amount = deposited_amount + term_of_the_deposit * \
               ((deposited_amount * annual_interest_rate / 100) / 12)
print(final_amount)