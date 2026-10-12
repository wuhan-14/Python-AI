def jc(n):
    if n!=1:
        return n*jc(n-1)
    else:
        return 1
print(jc(5))

print("-------------------------")

def calc_order_cost(*args, coupon=0, score=0, express=0.0):
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100
    total_cost += express
    return total_cost

total = calc_order_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 3999, 1), coupon=10, score=4000, express=9.9)
print(total)

total = calc_order_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 6999, 1), coupon=10, score=4000, express=9.9)
print(total)

total = calc_order_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 6999, 1), express=9.9)
print(total)

total = calc_order_cost(("鼠标", 88, 2),("键盘", 388, 1),("手机", 6999, 1))
print(total)