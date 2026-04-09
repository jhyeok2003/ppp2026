mart = {"우유": 2800, "계란": 300, "빵": 1200, "물": 1700}
cart = ["물", "물", "계란", "빵", "빵", "빵"]
total_cost = 0
for item in cart:
    total_cost += mart[item]
print("전부 다 해서 {:,}원을 지불해주세요.".format(total_cost))