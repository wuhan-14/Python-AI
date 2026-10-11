num_list=[]
for i in range(10):
    num=int(input("请输入一个数字:"))
    num_list.append(num)
print(num_list)
num_list.sort()
print(f"列表最小值为{num_list[0]},列表的最大值为{num_list[-1]},平均值为{sum(num_list)/len(num_list)}")
print(min(num_list))
print(max(num_list))