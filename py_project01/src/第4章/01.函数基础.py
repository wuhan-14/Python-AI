def out_line():
    print("-----------")
    print("-----------")

out_line()
out_line()

def circle_area(r):
    return 3.14*r*r

print(circle_area(5))

print("-------------------------")

def rectangle_area(l,w):
    return l*w

print(rectangle_area(20,10))

print("-------------------------")

def circle_area_len(r):
    return round(3.14*r*r,1),round(2*3.14*r,1)

print(circle_area_len(10))
area,len=circle_area_len(10)
print(area,len)

print("-------------------------")

def function_a():
    print("a ... before")
    function_b()
    print("a ... after")

def function_b():
    print("b ... before")
    function_c()
    print("b ... after")

def function_c():
    print("c ...")

function_a()
print("函数调用完毕 ~")