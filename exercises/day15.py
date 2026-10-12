# # 代码一
# # students = [
# #     {
# #         "name": "小明",
# #         "scores": [88, 92, 76],
# #     },
# #     {
# #         "name": "小红",
# #         "scores": [59, 60],
# #     },
# #     {
# #         "name": "小刚",
# #         "scores": [100, 85, 90],
# #     },
# # ]
# #
# # for student in students:
# #     print(f"学生：{student['name']}")
# #
# #     first = student["scores"][0]
# #     second = student["scores"][1]
# #     third = student["scores"][2]
# #
# #     total = first + second + third
# #     average = total / 3
# #
# #     print(f"第一门：{first}")
# #     print(f"第二门：{second}")
# #     print(f"第三门：{third}")
# #     print(f"总分：{total}")
# #     print(f"平均分：{average:.2f}")
# #     print("-" * 30)
# # 现象：打印小红时报错
# # 最后一行报错：IndexError: list index out of range
# # 错误类型：IndexError
# # 出错行：9
# # 根因：小红成绩没有输全三个，遍历仍然只是对三个成绩操作
# #修复代码
# students = [
#     {
#         "name": "小明",
#         "scores": [88, 92, 76],
#     },
#     {
#         "name": "小红",
#         "scores": [59, 60],
#     },
#     {
#         "name": "小刚",
#         "scores": [100, 85, 90],
#     },
# ]
#
# for student in students:
#     print(f"学生：{student['name']}")
#
#     scores = student["scores"]
#
#     total = sum(scores)
#     average = total / len(scores)
#
#     print(f"成绩：{scores}")
#     print(f"总分：{total}")
#     print(f"平均分：{average:.2f}")
#     print("-" * 30)
#
#
#
#
#
#
# # 代码二
# # contacts = [
# #     {
# #         "name": "小明",
# #         "phone": "13800000001",
# #         "email": "ming@example.com",
# #     },
# #     {
# #         "name": "小红",
# #         "phone": "13900000002",
# #         "email": "hong@example.com",
# #     },
# #     {
# #         "name": "小刚",
# #         "phone": "13700000003",
# #     },
# # ]
# #
# # for contact in contacts:
# #     name = contact["name"]
# #     phone = contact.get("phone", "无")
# #     email = contact["email"]
# #
# #     print(f"姓名：{name}")
# #     print(f"电话：{phone}")
# #     print(f"邮箱：{email}")
# #     print("-" * 30)
# # 现象：打印小刚内容时报错
# # 最后一行报错：KeyError: 'email'
# # 错误类型：KeyError
# # 出错行：59的循环或者55后没有写email
# # 根因：小刚没有email这个key但是后面遍历时依然包含
# # 修复方式：添加小刚的Email键值对"email": "gong@example.com"
# # 修复后输出：正常
#
# # 代码三
# # records = [
# #     {
# #         "name": "小明",
# #         "score": "88",
# #     },
# #     {
# #         "name": "小红",
# #         "score": 92,
# #     },
# #     {
# #         "name": "小刚",
# #         "score": "76",
# #     },
# #     {
# #         "name": "小丽",
# #         "score": 100,
# #     },
# # ]
# #
# # total = 0
# #
# # for record in records:
# #     total += record["score"]
# #     print(f"当前总分：{total}")
# #
# # average = total / len(records)
# #
# # print(f"总分：{total}")
# # print(f"平均分：{average:.2f}")
# # 现象：直接报错
# # 最后一行报错：TypeError: unsupported operand type(s) for +=: 'int' and 'str'
# # 错误类型：TypeError
# # 出错行：88
# # 根因：把成绩携程str形式，没有进行int转换处理
# #修复代码
# records = [
#     {
#         "name": "小明",
#         "score": "88",
#     },
#     {
#         "name": "小红",
#         "score": 92,
#     },
#     {
#         "name": "小刚",
#         "score": "76",
#     },
#     {
#         "name": "小丽",
#         "score": 100,
#     },
# ]
#
# total = 0
#
# for record in records:
#     total += int(record["score"])
#     print(f"当前总分：{total}")
#
# average = total / len(records)
#
# print(f"总分：{total}")
# print(f"平均分：{average:.2f}")
#
#
# #代码四
# # def summarize_scores(group_name, scores):
# #     total = sum(scores)
# #     average = total / len(scores)
# #     highest = max(scores)
# #     lowest = min(scores)
# #
# #     print(f"分组：{group_name}")
# #     print(f"总分：{total}")
# #     print(f"平均分：{average:.2f}")
# #     print(f"最高分：{highest}")
# #     print(f"最低分：{lowest}")
# #     print("-" * 30)
# #
# #
# # groups = {
# #     "第一组": [80, 90, 85],
# #     "第二组": [],
# #     "第三组": [60, 75, 88],
# # }
# #
# # for group_name, scores in groups.items():
# #     print(f"[DEBUG] 开始处理：{group_name}")
# #     print(f"[DEBUG] scores={scores!r}")
# #
# #     summarize_scores(group_name, scores)
# # 现象：运行到打印第二组内容时报错
# # 最后一行报错：ZeroDivisionError: division by zero
# # 错误类型：ZeroDivisionError
# # 出错行：131
# # 根因：没有应对成绩为零时的判断输出
# #修复代码
# def summarize_scores(group_name, scores):
#     if not scores:
#         print(f"分组：{group_name}")
#         print("没有成绩，无法统计")
#         return
#     total = sum(scores)
#     average = total / len(scores)
#     highest = max(scores)
#     lowest = min(scores)
#
#     print(f"分组：{group_name}")
#     print(f"总分：{total}")
#     print(f"平均分：{average:.2f}")
#     print(f"最高分：{highest}")
#     print(f"最低分：{lowest}")
#     print("-" * 30)
#
#
# groups = {
#     "第一组": [80, 90, 85],
#     "第二组": [],
#     "第三组": [60, 75, 88],
# }
#
# for group_name, scores in groups.items():
#     print(f"[DEBUG] 开始处理：{group_name}")
#     print(f"[DEBUG] scores={scores!r}")
#
#     summarize_scores(group_name, scores)
#
#
#
#
#
#
#
# #代码五
# # class Student:
# #     def __init__(self, name, ch_score, ma_score, en_score):
# #         self.name = name
# #         self.chscore = ch_score
# #         self.mascore = ma_score
# #         self.enscore = en_score
# #
# #     def average_score(self):
# #         total = self.chscore + self.mascore + self.enscore
# #
# #         return total / 3
# #
# #     def __str__(self):
# #         return (
# #             f"姓名：{self.name} | "
# #             f"语文：{self.chscore} | "
# #             f"数学：{self.mascore} | "
# #             f"英语：{self.enscore}"
# #         )
# #
# #
# # students = [
# #     Student("小明", 88, 76, 90),
# #     Student("小红", 95, 89, 92),
# #     Student("小华", 59, 60, 45),
# # ]
# #
# # for student in students:
# #     print(student)
# #     print(dir(student))
# #     print(f"平均分：{student.average():.2f}")
# #     print("-" * 30)
# # 现象：打印平均分时出错
# # 最后一行报错：AttributeError: 'Student' object has no attribute 'average'
# # 错误类型：AttributeError
# # 出错行：179
# # 根因：把average_score函数写成average()
# # 修复方式：print(f"平均分：{student.average_score():.2f}")
# # 修复后输出：正常





#进阶
# response = {
#     "code": 0,
#     "message": "success",
#     "data": {
#         "users": [
#             {
#                 "id": 1,
#                 "name": "小明",
#                 "profile": {
#                     "city": "北京",
#                     "phone": "13800000001",
#                 },
#             },
#             {
#                 "id": 2,
#                 "name": "小红",
#                 "profile": {},#这里少东西
#             },
#             {
#                 "id": 3,
#                 "name": "小刚",#还有这里
#             },
#         ]
#     },
# }
#
# for user in response["data"]["users"]:
#     user_id = user["id"]
#     name = user["name"]
#     city = user["profile"]["city"]
#     phone = user["profile"]["phone"]
#
# print(f"用户ID：{user_id}")
# print(f"姓名：{name}")
# print(f"城市：{city}")
# print(f"电话：{phone}")
# print("-" * 30)


response = {
    "code": 0,
    "message": "success",
    "data": {
        "users": [
            {
                "id": 1,
                "name": "小明",
                "profile": {
                    "city": "北京",
                    "phone": "13800000001",
                },
            },
            {
                "id": 2,
                "name": "小红",
                "profile": {},#这里少东西
            },
            {
                "id": 3,
                "name": "小刚",#还有这里
            },
        ]
    },
}

def get_profile_field(user, field_name, default_value):
    try:
        profile = user["profile"]
        return profile[field_name]

    except KeyError:
        return default_value

    except TypeError:
        return default_value


users = response["data"]["users"]

for user in users:
    user_id = user.get("id", "未知")
    name = user.get("name", "未知")

    city = get_profile_field(user, "city", "未知")
    phone = get_profile_field(user, "phone", "未提供")

    print(f"用户ID：{user_id}")
    print(f"姓名：{name}")
    print(f"城市：{city}")
    print(f"电话：{phone}")
    print("-" * 30)
