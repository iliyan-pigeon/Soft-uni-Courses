junior_competitors = int(input())
senior_competitors = int(input())
route_type = input()
junior_price = 0
senior_price = 0
total_junior = 0
total_senior = 0
total_price = 0
costs_price = 0
final_price = 0
if route_type == "trail":
    junior_price = 5.5
    senior_price = 7
    total_junior = junior_price * junior_competitors
    total_senior = senior_price * senior_competitors
    total_price =  total_junior + total_senior
elif route_type == "cross-country":
    junior_price = 8
    senior_price = 9.5
    if junior_competitors + senior_competitors >= 50:
        junior_price = junior_price - (junior_price * 0.25)
        senior_price = senior_price - (senior_price * 0.25)
    total_junior = junior_price * junior_competitors
    total_senior = senior_price * senior_competitors
    total_price = total_junior + total_senior
elif route_type == "downhill":
    junior_price = 12.25
    senior_price = 13.75
    total_junior = junior_price * junior_competitors
    total_senior = senior_price * senior_competitors
    total_price = total_junior + total_senior
elif route_type == "road":
    junior_price = 20
    senior_price = 21.5
    total_junior = junior_price * junior_competitors
    total_senior = senior_price * senior_competitors
    total_price = total_junior + total_senior
costs_price = total_price * 0.05
final_price = total_price - costs_price
print(f"{final_price:.2f}")
