s="Hello-Python-Hello-World"

print(s[4])
print(s[-8])

for i in s:
    print(i,end=" ")
print()

print(s[0:5:1])
print(s[:5:1])
print(s[0:5])
print(s[:5])

print(s[6:12:1])
print(s[6::1])

print(s[0:5:2])
print(s[-1:-7:-1])
print(s[::-1])

print(s.find("P"))
print(s.count("o"))
print(s.upper())
print(s.lower())
print(s.split("-"))
print(s.replace("-","_"))

print(s.startswith("Hello"))
print(s.endswith("Python"))

ss="   123   "
print(ss.strip())