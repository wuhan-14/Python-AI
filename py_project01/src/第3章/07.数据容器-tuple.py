t1=(80,95,78,50,76,80,56,85,20)

print(t1)
print(type(t1))

print("-------------------------")

print(t1[0])
print(t1[-1])

print(t1[0:5:1])

print("-------------------------")

print(t1.count(80))
print(t1.index(80))

print("-------------------------")

t2=()
print(t2)
print(type(t2))

t3=(100,)
print(t3)
print(type(t3))

print("-------------------------")

t1=(5,7,9,10,2,23,12)
t2=5,7,9,10,2,23,12

print(t1)
print(t2)

print("-------------------------")

a,b,c,d,e,f,g=t1
print(a,b,c,d,e,f,g)
first,second,*other,last=t1
print(first,second,other,last)
print(type(first),type(other))

print("-------------------------")

a=10
b=20
#t=b,a
#a,b=t
a,b=b,a
print(a,b)

a=100
b=200
c=300
a,b,c=b,c,a
print(a,b,c)