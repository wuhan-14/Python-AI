class Car:
    pass

c1=Car()
c1.brand="BMW"
c1.name="X5"
c1.price=500000
print(c1)
print(c1.__dict__)

print("-------------------------")

class Car:
    def __init__(self,c_brand,c_name,c_price):
        self.brand=c_brand
        self.name=c_name
        self.price=c_price

c1=Car("BMW","X5",500000)
print(c1.__dict__)
c2=Car("奔驰","e300",450000)
print(c2.__dict__)

print("-------------------------")

class Car:
    def __init__(self,c_brand,c_name,c_price):
        self.brand=c_brand
        self.name=c_name
        self.price=c_price
    def running(self):
        print(f"{self.brand}{self.name}正在高速行驶")
    def total_cost(self,discount,rate):
        total_cost=self.price*discount+self.price*rate
        return total_cost

c1=Car("BMW","X5",500000)
c1.running()
print(c1.total_cost(0.9,0.1))

print("-------------------------")

class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕, 对象属性已经添加完毕 .")

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中....")
    def total_cost(self, discount, rate=0.1):
        total_cost = self.price * discount + rate * self.price
        return total_cost
    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"
    def __eq__(self, other):
        return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
    def __lt__(self, other):
        return self.price < other.price

c1 = Car("白色", "BYD", "汉", 180000)
print(c1)

c2 = Car("白色", "BYD", "汉", 180000)
print(c2)

c3 = Car("白色", "BYD", "汉", 180001)
print(c3)

print(c1 == c2)
print(c1 > c3)

print("-------------------------")

class Car:
    wheel = 2
    tax_rate = 0.1 

    def __init__(self, c_color, c_brand, c_name, c_price, c_wheel):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.wheel = c_wheel

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中....")

    def total_cost(self, discount, rate=0.1):
        total_cost = self.price * discount + rate * self.price
        return total_cost

c1 = Car("白色", "BYD", "汉", 180000, 4)
print(c1.brand)
print(c1.wheel) 

print(Car.wheel)

c2 = Car("黑色", "Tesla", "Model Y", 260000, 4)
print(c2)