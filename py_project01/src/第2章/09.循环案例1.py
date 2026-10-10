while True:
    username=input("请输入用户名:")
    password=input("请输入密码:")
    if username=="" or password=="":
        print("用户名或密码不能为空")
        continue
    elif username=="admin" and password=="666888":
        print("登陆成功")
        break
    elif username=="root" and password=="777888":
        print("登陆成功")
        break
    else:
        print("用户名或密码错误，请重新输入")