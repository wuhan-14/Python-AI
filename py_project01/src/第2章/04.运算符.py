print("10 + 4 = ",10 + 4)
print("10 - 4 = ",10 - 4)
print("10 * 4 = ",10 * 4)
print("10 / 4 = ",10 / 4)
print("10 // 4 = ",10 // 4)
print("10 % 4 = ",10 % 4)
print("10 ** 4 = ",10 ** 4)

print("0.1 + 10 / 4**2 = ",0.1 + 10 / 4**2)

print("-------------------------")

x = float(input("请输入x的值："))
y = float(input("请输入y的值："))
print("x + y = ",x + y)
print("x - y = ",x - y)

print("-------------------------")

num = 85
num += 10
print("num += 10 后，num = ",num)
num -= 10
print("num -= 10 后，num = ",num)
num *= 10
print("num *= 10 后，num = ",num)
num /= 10
print("num /= 10 后，num = ",num)
num //= 10
print("num //= 10 后，num = ",num)
num %= 3
print("num %= 3 后，num = ",num)
num **= 3
print("num **= 3 后，num = ",num)

print("-------------------------")

print("100 == 100 ：",100 == 100)
print("'100' == '100' ：","100" == "100")
print("100 != 100 ：",100 != 100)
print("100 < 100 吗：",100 < 100)
print("100 <= 100 吗：",100 <= 100)
print("100 > 100 吗：",100 > 100)
print("100 >= 100 吗：",100 >= 100)

print("-------------------------")

n = int(input("请输入一个整数："))
print(f"{n}在10-20之间：", n >= 10 and n <= 20)
print(f"{n}在10-20之间：", 10 <= n <= 20)
m=int(input("请输入一个整数: "))
print(f"{n}不在10-20之间：", m < 10 or m > 20)