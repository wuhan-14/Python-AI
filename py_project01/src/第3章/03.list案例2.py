num_list1=[54,20,123,54]
num_list2=[80,123,54,29,91]
for num in num_list2:
    num_list1.append(num)
print(num_list1)
new_list=[]
for num in num_list1:
    if num not in new_list:
        new_list.append(num)
print(new_list)

num_list1=[54,20,123,54]
num_list2=[80,123,54,29,91]
num_list=[*num_list1,*num_list2]
print(num_list)
new_list=[]
for num in num_list:
    if num not in new_list:
        new_list.append(num)
print(new_list)

num_list1=[54,20,123,54]
num_list2=[80,123,54,29,91]
num_list=num_list1+num_list2
print(num_list)
new_list=[]
for num in num_list:
    if num not in new_list:
        new_list.append(num)
print(new_list)