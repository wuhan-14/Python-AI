mail=input("请输入一个邮箱:")
if mail.count("@")==1 and mail.count(".")>=1:
    print("这是一个合法的邮箱")
else:
    print("这不是一个合法邮箱")
if mail.count("@")==1 and "." in mail:
    print("这是一个合法的邮箱")
else:
    print("这不是一个合法邮箱")

print("-------------------------")

s=input("请输入一个字符串:")
if s==s[::-1]:
    print("这是一个回文串")
else:
    print("这不是一个回文串")

print("-------------------------")

list=[]
for i in range(10):
    s=input("请输入一个字符串:")
    list.append(s[::-1].upper())
print(list)