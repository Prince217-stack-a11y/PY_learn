#C1. 变量、输入与输出
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if b == 0:
    print("Error: Division by zero is not allowed.")
else:
    print(f"加法: {a + b}")
    print(f"减法: {a - b}")
    print(f"乘法: {a * b}")
    print(f"除法: {a / b}")
# # #C2. 字符串
str = ("2026-09-12 10:35:20 ERROR Disk full")
date = str[0]
level = str[2]
msg = str[3|4]
print(date)
print(level)
print(msg)
str_1 = [i for i in str if "ERROR" in str]
print(str_1)

# #C3. list
# #1
scores = [88, 59, 92, 71, 45, 100]
avg = sum(scores) / len(scores)
print(avg)
#2
scores.sort()
print(scores[0],scores[-1])

total = 0
for score in scores:
    if score <= 60:
        total += 1
print(total)
#4
for i, score in enumerate(scores,start=1):
    print(i, score)
#5
passed_score = [i for i in scores if i >= 60]
print(passed_score)

# #C4.dict
dict1 = {}
dict1["张三"] = 19922021998
dict1["李四"] = 18820282022
print(dict1)
dict1["张三"] = 2
print(dict1)
del dict1["张三"]
print(dict1.items())
#值是value，键是key，值通过键进行定位找寻以及其它操作
#C5
students = [
    {"name": "小明", "score": 88},
    {"name": "小红", "score": 59},
    {"name": "小刚", "score": 76},
]
print(f"{students[0]} {students[1]} {students[2]}")
print(f"平均分为：{sum(88,59,76)/3}")
#打印不及格学生不会