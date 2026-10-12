a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E", 100]
phones = {"13309091111", "15209101902", "18809019201"}
options = {"count":2 , "total":10}
goods = ("手机", 6999, 1)

names.append("X")
names.append(10010)
names.append(10010.0)

print(names)

a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str | int] = ["A", "C", "E"]
phones2: set[str] = {"13309091111", "15209101902", "18809019201"}
options2: dict[str, int] = {"count":2 , "total":10}
goods2: tuple[str, int, int] = ("手机", 6999, 1)

names2.append("X")
names2.append(10010)
names2.append(10010.0)

print(names2)

print("-------------------------")

def circle_area_len(r: float) -> tuple[float, float]:
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)


al = circle_area_len(8.5)
print(al)



def calc_order_cost(*args:tuple[str, float, int], coupon:int=0, score:int=0, express:float=0.0) -> float:
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100
    total_cost += express
    return total_cost

total = calc_order_cost(("鼠标", 88.5, 2),("键盘", 388, 1),("手机", 6999, 1))
print(total)