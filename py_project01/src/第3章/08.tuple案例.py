students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")

for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]} \t{s[1]}\t{s[2]} \t{s[3]} \t{s[4]} \t{total} \t{avg:.1f}")

print("-------------------------")

chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]

print(f"语文最低分: {min(chinese_scores)}, 最高分: {max(chinese_scores)}, 平均分: {sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分: {min(math_scores)}, 最高分: {max(math_scores)}, 平均分: {sum(math_scores)/len(math_scores)}")
print(f"英语最低分: {min(english_scores)}, 最高分: {max(english_scores)}, 平均分: {sum(english_scores)/len(english_scores)}")

print("-------------------------")

print("优秀学生(平均分 > 90)名单如下：")
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 90:
        print(f"学号: {s[0]}, 姓名: {s[1]}, 平均分: {avg}")

print()

print("-------------------------")

students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")

for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t{name} \t{chinese} \t{math} \t{english} \t{total} \t{avg:.1f}")

print()

print("-------------------------")

chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]

print(f"语文最低分: {min(chinese_scores)}, 最高分: {max(chinese_scores)}, 平均分: {sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分: {min(math_scores)}, 最高分: {max(math_scores)}, 平均分: {sum(math_scores)/len(math_scores)}")
print(f"英语最低分: {min(english_scores)}, 最高分: {max(english_scores)}, 平均分: {sum(english_scores)/len(english_scores)}")

print("-------------------------")

print("优秀学生(平均分 > 90)名单如下：")
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"学号: {id}, 姓名: {name}, 平均分: {avg:.1f}")