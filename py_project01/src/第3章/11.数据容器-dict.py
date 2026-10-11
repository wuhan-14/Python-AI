dict1 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688}
print(dict1)
print(type(dict1))

dict2 = {0:670, 1.5:608, (1,2):580, ('A','B'):688}
print(dict2)

print(dict1["李慕婉"])
dict1["李慕婉"] = 688
print(dict1)

dict1["涛哥"]=600
print(dict1)
dict1["涛哥"]=550
print(dict1)

print(dict1["涛哥"])
print(dict1.get("涛哥"))

print(dict1.keys())
print(dict1.values())
print(dict1.items())

score=dict1.pop("徐立国")
print(score)
print(dict1)
del dict1["涛哥"]
print(dict1)

for k in dict1.keys():
    print(f"{k} : {dict1[k]}")

for item in dict1.items():
    print(f"{item[0]} : {item[1]}")

for key,values in dict1.items():
    print(f"{key} : {values}")