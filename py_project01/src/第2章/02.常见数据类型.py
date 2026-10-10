print(type("Hello"))
print(type(100))
print(type(3.14))
print(type(True))
print(type(None))
a=100
print(type(a))
print(isinstance(a, int))
print(isinstance(a, float))
print(isinstance(a, bool))

s1="Hello"
s2='Python'
s3="""
Hello:
       欢迎学习Python
       加油！
"""
print(s1)
print(s2)
print(s3)
print(type(s1))
print(type(s2))
print(type(s3))

msg1='It\'s a dog'
print(msg1)
msg2="It's a dog"
print(msg2)

msg3="Hello的意思是\"你好\""
print(msg3)
msg4='Hello的意思是"你好"'
print(msg4)

print("\t欢迎学习Python\n\t加油努力")

s1="人生苦短""我用Python"",OK"
print(s1)
s2="人生苦短"+"我用Python"+",OK"
print(s2)
msg1="人生苦短"
msg2="我学Python"
print("我说:"+msg1+msg2)

name="王五"
age=20
pro="软件工程"
hobby="Python,Java"
print("我是"+name+",我今年"+str(age)+"岁,我的专业是"+pro+",我喜欢的语言是"+hobby)
print("我是%s,我今年%s岁,我的专业是%s,我喜欢的语言是%s"%(name,age,pro,hobby))
print(f"我是{name},我今年{age}岁,我的专业是{pro},我喜欢的语言是{hobby}")