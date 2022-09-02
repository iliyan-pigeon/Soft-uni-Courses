price_sq_m = 7.61
discount_volume = 0.18
sq_m_volume = float(input())
full_price = price_sq_m * sq_m_volume
discount = full_price * discount_volume
final_price = full_price - discount
print(f'The final price is: {final_price} lv.' )
print(f'The discount is: {discount} lv.')



