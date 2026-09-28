# names = ["小明", "小红", "小明", "小丽"]
#
# unique_names = set(names)
#
# print(unique_names)

all_students = ["小明", "小红", "小刚", "小丽", "小华", "小周"]#应到名单
present_students = ["小明", "小刚", "小丽", "小华", "小刘", "小明"]#实际打卡名单

all_set = set(all_students)
present_set = set(present_students)
should_butnot = all_set - present_set
print(f"缺勤学生为{should_butnot}")

not_shouldin = present_set - all_set
print(f"不应在名单中人为;{not_shouldin}")

present_in_roster = present_set & all_set
present_count = len(present_in_roster)
all_count = len(all_set)
attendance_rate = present_count / all_count * 100

print(f"有效实到人数：{present_count}")
print(f"应到人数：{all_count}")
print(f"实到率：{attendance_rate:.2f}%")

#为下面场景选择 list、tuple、dict、set
# 1. 保存一天中按时间记录的温度->list
# 2. 保存固定坐标 (100, 200)->tuple
# 3. 保存姓名和电话号码的对应关系->dict
# 4. 从大量数据中去掉重复值->set
# 5. 判断某个人是否已经在名单中->set
