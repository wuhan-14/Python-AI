import random
random_num=random.randint(1,100)
print(random_num)
count=0
while True:
    guess_num=int(input("请输入一个数字:"))
    if guess_num<random_num:
        print("数字猜小了")
        count+=1
        continue
    elif guess_num>random_num:
        print("数字猜大了")
        count+=1
        continue
    else:
        print(f"恭喜你猜对了,一共猜了{count+1}次")
        break
    