s1={5,3,2,0,9,12,43,64,22,5,0}

print(s1)
print(type(s1))

s2=set()
print(s2)
print(type(s2))

s1={100,200,300,400,500,600,700,800}

s1.add(900)
print(s1)

s1.remove(200)
print(s1)

num=s1.pop()
print(s1,num)

s1.clear()
print(s1)
print(type(s1))

s1={'A','B','C','E','X','Y'}
s2={'D','E','Y','Z'}
print(s1.difference(s2))
print(s2.difference(s1))

print(s1.union(s2))

print(s1.intersection(s2))