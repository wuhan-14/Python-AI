score=685
if score>680:
    print("欢迎你来到清华读书")
    print("也恭喜你踏入精彩的大学生活")

print("-------------------------")

ok_account="123456"
ok_password="123456"
account=input("请输入账号:")
password=input("请输入密码:")
if account==ok_account and password==ok_password:
    print("登陆成功")
    print("欢迎进入")
if account!=ok_account or password!=ok_password:
    print("登陆失败")
    print("账号或密码错误")
    
if account==ok_account and password==ok_password:
    print("登陆成功")
    print("欢迎进入")
else:
    print("登陆失败")
    print("账号或密码错误")

print("-------------------------")
    
year=int(input("请输入一个年份:"))
if (year%4==0 and year%100!=0)or (year%400==0):
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")

print("-------------------------")

num=int(input("请输入一个整数:"))
if num>0:
    print(f"{num}是一个正数")
elif num<0:
    print(f"{num}是一个负数")
else:
    print(f"{num}是'0'")

print("-------------------------")

username=input("请输入用户名:")
password=input("请输入密码:")
if username=="admin" and password=="666888":
    print("登陆成功")
elif username=="root" and password=="777888":
    print("登陆成功")
elif username=="zhangsan" and password=="888888":
    print("登陆成功")
else:
    print("登陆失败,账号或密码错误")

print("-------------------------")

a=int(input("请输入第一条边边长:"))
b=int(input("请输入第二条边边长:"))
c=int(input("请输入第三条边边长:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("这是一个等边三角形")
    elif a==b or a==c or b==c:
        print("这是一个等腰三角形")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("这是一个直角三角形")
    else:
        print("这是一个普通的三角形")
else:
    print("三条边不能构成一个三角形")