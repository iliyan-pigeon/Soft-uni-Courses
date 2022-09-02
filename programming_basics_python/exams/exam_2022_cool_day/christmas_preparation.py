rollers_paper_number = int(input())
rollers_plat_number = int(input())
litres_glue = float(input())
percent_discount = int(input())
roller_paper_price = 5.8
roller_plat_price = 7.2
litre_glue_price = 1.2
total_paper_price = rollers_paper_number * roller_paper_price
total_plat_price = rollers_plat_number * roller_plat_price
total_glue_price = litres_glue * litre_glue_price
total_price = total_paper_price + total_plat_price + total_glue_price
discount = total_price * (percent_discount / 100)
final_price = total_price - discount
print(f"{final_price:.3f}")

