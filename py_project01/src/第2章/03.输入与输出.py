name=input("请输入你的姓名:")
age=input("请输入你的年龄:")
pro=input("请输入你的专业:")
hobby=input("请输入你喜欢的语言:")
print(f"我是{name},我今年{age}岁,我的专业是{pro},我喜欢的语言是{hobby}")

print("-------------------------")

total=10000
password=input("请输入密码:")
print("密码正确")
num=input("输入你要取款的金额:")
print(f"你的银行卡余额为{total-int(num)}")