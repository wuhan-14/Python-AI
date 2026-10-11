num_list1=[]
for i in range(1,21):
    num_list1.append(i**2)
print(num_list1)

#列表推导式格式1:[要插入的值 for i in 序列/列表]

num_list2=[]
num_list2=[i**2 for i in range(1,21)]
print(num_list2)

#列表推导式格式2:[要插入的值 for i in 序列/列表 if 条件]

num_list3=[12,32,45,77,80,92,33,57,97,98,110,111,122]
new_list=[num**2 for num in num_list3 if num%2==0]
print(new_list)