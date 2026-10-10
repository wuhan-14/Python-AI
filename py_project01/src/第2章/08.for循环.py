msg=input("请输入需要遍历的字符串:")

for s in msg:
    print(s)
else:
    print("遍历结束")

sum=0
for i in range(1,101):
    if i%2!=0:
        sum+=i
print(sum)

sum=0
for i in range(1,101,2):
    sum+=i
print(sum)

sum=0
for i in range(100,501):
    if i%3==0:
        sum+=i
print(sum)

m=int(input("请输入长度:"))
n=int(input("请输入宽度:"))
for _ in range(n):
    for _ in range(m):
        print("*",end="  ")
    print("\n")

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end="\t")
    print()