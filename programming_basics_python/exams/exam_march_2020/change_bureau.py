amount_bitcoin = int(input())
amount_yuan = float(input())
commission_percent = float(input())
course_bitcoin_lev = 1168
course_yuan_dollar = 0.15
course_dollar_lev = 1.76
course_euro_lev = 1.95
bitcoin_in_lev = amount_bitcoin * course_bitcoin_lev
bitcoin_in_euro = bitcoin_in_lev / course_euro_lev
yuan_in_dollar = amount_yuan * course_yuan_dollar
yuan_in_lev = yuan_in_dollar * course_dollar_lev
yuan_in_euro = yuan_in_lev / course_euro_lev
total_amount = yuan_in_euro + bitcoin_in_euro
commission_amount = total_amount * commission_percent / 100
final_amount = total_amount - commission_amount
print(f"{final_amount:.2f}")
