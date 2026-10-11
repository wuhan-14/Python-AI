s=[50,90,88,65,90,"A","Hello",True]

print(type(s))

print(s[0])
print(s[-8])

print(s[2])
print(s[-6])

s[5]="ABC"
print(s)

del s[6]
print(s)

for item in s:
    print(item,end=" ")

s=["A","C","H","K","L","B","D","X","C","U"]

#s[开始索引:结束索引:步长]

print(s[0:5:1])
print(type(s[0:5:1]))

print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[0:5:2])
print(s[0:-2:1])

s=[56,90,88,65,90,100,209,72,145]
s.append(188)
print(s)
s.insert(2,80)
print(s)
s.remove(90)
print(s)
num=s.pop(1)
print(num)
print(s)
s.sort()
print(s)
s.reverse()
print(s)