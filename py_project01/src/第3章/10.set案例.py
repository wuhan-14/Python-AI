football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

fa_set = french_set.intersection(art_set)
print(f"同时选修了法语和艺术的学生:\n {fa_set}")

fa_set2 = french_set & art_set
print(f"同时选修了法语和艺术的学生:\n {fa_set2}")

all_set = football_set & basketball_set & french_set & art_set
print(f"同时选修了所有四门课程的学生:\n {all_set}")

fb_set = football_set.difference(basketball_set)
print(f"选修了足球，但是没有选修篮球的学生:\n {fb_set}")

fb_set2 = football_set - basketball_set
print(f"选修了足球，但是没有选修篮球的学生:\n {fb_set2}")

fb_set3 = {s for s in football_set if s not in basketball_set}
print(f"选修了足球，但是没有选修篮球的学生:\n {fb_set3}")

print("-------------------------")

all_set = football_set | basketball_set | french_set | art_set

all_list = [*football_set, *basketball_set, *french_set, *art_set]

for s in all_set:
    print(f"{s} \t选修了 {all_list.count(s)} 课程")