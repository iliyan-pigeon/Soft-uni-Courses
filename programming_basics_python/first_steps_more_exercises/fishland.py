mackerel_price_kg = float(input())
sprat_price_kg = float(input())
amito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())
amito_price_kg = mackerel_price_kg + \
                 (mackerel_price_kg * 60 / 100)
horse_mackerel_price_kg = sprat_price_kg + \
                    (sprat_price_kg * 80 / 100)
mussels_price_kg = 7.5
amito_total_price = amito_kg * amito_price_kg
horse_macherel_total_price = horse_mackerel_kg * horse_mackerel_price_kg
mussels_total_price = mussels_kg * mussels_price_kg
total_price = amito_total_price + horse_macherel_total_price \
    + mussels_total_price
print(f'{total_price:.2f}')