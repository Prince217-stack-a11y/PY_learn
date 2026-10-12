

stu_list = [{"name": "小明","scores": 90},
            {"name": "小红","scores": 98},
            {"name": "小刚","scores": 96},
            {"name": "小丽","scores": 60},
            {"name": "小华","scores": 12}]
print(stu_list)
print()
stu_list.append({"name": "小刘","scores": 100})
print(stu_list)
print()
stu_list.insert(2, {"name": "小周","scores": 20})
print(stu_list)
print()
stu_list[2]["scores"] = 10
print(stu_list)
print()
remove = stu_list.pop(3)
print(remove)
print(stu_list)
print()

total = 0
unpassed_students = []
for stu in stu_list:
    for key, value in stu.items():
        if key == "scores":
            total += value

    if stu["scores"] < 60:
        unpassed_students.append(stu["name"])

print(f"不及格名单为：{unpassed_students}")

print(f"平均分为：{round(total / len(stu_list), 2)}")
print()
query_name = input("请输入学生姓名：")
found = False

for stu in stu_list:
    if stu["name"] == query_name:
        print(f"姓名：{stu['name']}")
        print(f"成绩：{stu['scores']}")
        found = True
        break

if not found:
    print("未找到该学生")











