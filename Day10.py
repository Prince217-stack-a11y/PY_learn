# scores = [88, 59, 92, 71, 45, 100, 60, 76, 59, 0]
#
# #平均分
# def calc_avg(score):
#     return sum(scores) / len(scores)
#
# #最高分
# def calc_max(score):
#     return max(scores)
#
# #最低分
# def calc_min(score):
#     return min(scores)
#
# #综合
# def calc_num(scores):
#     return sum(scores) / len(scores),max(scores),min(scores)
#
# avg, max_num, min_num = calc_num(scores)
# #下面的和上面的综合分开运行
# # avg = calc_avg(scores)
# # max = calc_max(scores)
# # min = calc_min(scores)
#
# print(f"最高分为{max_num},最低分为{min_num},平均分为{avg}")



#--------拆分
#案例一
#原函数
# width = 4
# height = 5
#
# area = width * height
# perimeter = 2 * (width + height)
#
# print(f"面积：{area}")
# print(f"周长：{perimeter}")
#修改
# def calc_area(width, height):
#     return width * height
# def calc_perimeter(width, height):
#     return 2 * (width + height)
# def print_rectangle_report(width, height):
#     print(f"面积：{calc_area(width, height)}, 周长：{calc_perimeter(width, height)}")
#
# print_rectangle_report(20,39)



#案例二
# #原函数
# scores = [88, 59, 92, 71, 45, 100, 60, 76, 59, 0]
#
# total = 0
# for score in scores:
#     total += score
#
# average = total / len(scores)
#
# failed = []
# for score in scores:
#     if score < 60:
#         failed.append(score)
#
# print(f"最高分：{max(scores)}")
# print(f"最低分：{min(scores)}")
# print(f"平均分：{average}")
# print(f"不及格成绩：{failed}")
#修改
# def clac_avg(score):
#     return sum(scores)/len(scores)
# def get_failed_scores(score):
#     failed_stu = []
#     for score in scores:
#         if score <60:
#             failed_stu.append(score)
#     return failed_stu
# def calc_score(score):
#     avg = clac_avg(scores)
#     failed_stu = get_failed_scores(scores)
#     print(f"最高分为{max(scores)},最低分为{min(scores)}")
#     print(f"平均分为{avg}")
#     print(f"不及格成绩为{failed_stu}")
#
# calc_score(scores)

#案例三
#原函数
# todos = [
#     {"title": "学习函数", "done": False},
#     {"title": "完成练习", "done": True},
# ]
#修改
# def add_todo(todos, title):
#     for todo in todos:
#         if todo["title"] == title:
#             return False
#
#     todos.append({
#         "title": title,
#         "done": False,
#     })
#     return True
#
#
#
#
# def print_todos(todos):
#     for todo in todos:
#         mark = "[x]" if todo["done"] else "[ ]"
#         print(f"{mark} {todo['title']}")
#
#
# todos = [
#     {"title": "学习函数", "done": False},
#     {"title": "完成练习", "done": True},
# ]
#
# add_todo(todos, "完成 Day 10")
#
# print_todos(todos)

