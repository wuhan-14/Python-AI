def triangle_area(b,h):
    return b*h/2

print(triangle_area(10,10))

print("-------------------------")

def count_aeiou(str):
    num=0
    for s in str:
        if s in "aeiouAEIOU":
            num+=1
    return num

print(count_aeiou("Hello-World-Hello-Python"))

print("-------------------------")

def calc_score(score_list):
    return max(score_list),min(score_list),round(sum(score_list)/len(score_list),1)

s_list=[605,660,580,720,702,439]
print(calc_score(s_list))