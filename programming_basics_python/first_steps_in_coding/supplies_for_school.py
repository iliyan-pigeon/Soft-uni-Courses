price_packet_pens = 5.80
price_packet_markers = 7.20
price_cleaner_per_litre = 1.20
amount_packet_pens = int(input())
amount_packet_markers = int(input())
litres_of_cleaner = int( input())
percent_discount = int(input())
pens_total_price = price_packet_pens * amount_packet_pens
markers_total_price = price_packet_markers * amount_packet_markers
cleaner_total_price = price_cleaner_per_litre * litres_of_cleaner
total_price = pens_total_price + markers_total_price + cleaner_total_price
discount = total_price * percent_discount/100
final_price = total_price - discount
print(final_price)