num1 = 100
print("num1 = ",num1)
def circle_area(r):
    pi = 3.14
    area = pi * r * r
    num1=10000
    print("num1 = ", num1)
    return area

c_area = circle_area(10)
print(c_area)
print("num1 = ", num1)

print("-------------------------")

num2 = 200
print("num2 = ",num2)
def circle_area(r):
    pi = 3.14
    area = pi * r * r
    global num2
    num2=20000
    print("num2 = ", num2)
    return area

c_area = circle_area(10)
print(c_area)
print("num2 = ", num2)

print("-------------------------")

def reg_stu(name, age, gender, city):
    print(f"注册成功, 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

stu = reg_stu("张三", 18, "男", "北京")
print(stu)

stu = reg_stu(name="王林", age=28, gender="男", city="北京")
print(stu)

stu = reg_stu(age=20, gender="女", city="北京", name="李慕婉")
print(stu)

stu = reg_stu("李慕婉", 20, gender="女", city="北京")
print(stu)

print("-------------------------")

def reg_stu(name, age, gender="男", city="北京"):
    print(f"注册成功, 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

stu = reg_stu("王林", 20)
print(stu)

stu = reg_stu("李慕婉", 18, "女")
print(stu)

stu = reg_stu("韩立", 22, city="上海")
print(stu)

print("-------------------------")

def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data, max_data, round(avg_data, 1)

print(calc_data(2, 7, 9, 10, 45))

print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222))

print("-------------------------")

def calc_data(*args, **kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))

    if kwargs.get("print"):
        print(f"计算出来的最小值: {min_data}, 最大值: {max_data}, 平均值:{avg_data}")

    return min_data, max_data, avg_data

print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222, round=3, print=True))

print("-------------------------")

print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222, print=False))

print("-------------------------")

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def cacl(x,y,oper):
    return oper(x,y)

print(add(10,20))
print(multiply(10,20))
print(cacl(10,20,add))
print(cacl(10,20,multiply))

print("-------------------------")

out_line=lambda : print("已执行")
out_line()

add=lambda x,y:x+y
print(add(20,30))

data_list=["C++","C","Python","Jack","PHP","Java","Go","JavaScript","Rust"]
print(data_list)

data_list.sort(key=lambda item:len(item),reverse=True)
print(data_list)