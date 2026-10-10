student_group = {}
menu = """
####################################【菜单】#############################################
# 1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询学生信息 5.列出所有学生 6.统计班级成绩 7.退出系统 #
#######################################################################################
"""

def stu_add(name):
    if name in student_group:
        print("该学生已存在")
    else:
        student_scr_ch = int(input("请输入学生语文成绩："))
        student_scr_ma = int(input("请输入学生数学成绩："))
        student_scr_en = int(input("请输入学生英语成绩："))
        student_group[student_name] = {"Chinese Score": student_scr_ch, "Math Score": student_scr_ma,
                                       "English Score": student_scr_en}
        print("已完成！")


def update_stu(name):
    if name not in student_group:
        print("该学生不存在！")
    else:
        student_scr_ch = int(input("请输入学生新语文成绩："))
        student_scr_ma = int(input("请输入学生新数学成绩："))
        student_scr_en = int(input("请输入学生新英语成绩："))
        student_group[student_name] = {"Chinese Score": student_scr_ch, "Math Score": student_scr_ma,
                                       "English Score": student_scr_en}
        print("修改完毕")

def del_stu(name):
    if name not in student_group:
        print("该学生不存在！")
    else:
        del student_group[student_name]
        print("删除完毕")

def search_stu(name):
    if name not in student_group:
        if student_name in student_group:
            info = student_group[student_name]
            print(f"{info}")
        else:
            print("该学生不存在！")

def show_all():
    if not student_group:
        print("暂无学生信息")
    else:
        print("===== 所有学生信息 =====")
        for name, scores in student_group.items():
            print(
                f"姓名：{name} | 语文：{scores['Chinese Score']} 数学：{scores['Math Score']} 英语：{scores['English Score']}")

def calc_all():
    if not student_group:
        print("暂无学生数据，无法统计")
    else:
        # 1. 收集所有学生的各科成绩 + 姓名对应关系
        chinese_list = []
        math_list = []
        english_list = []
        for name, scores in student_group.items():  # 按序先把名字赋值给name，再把成绩赋值给scores
            chinese_list.append((scores['Chinese Score'], name))
            math_list.append((scores['Math Score'], name))
            english_list.append((scores['English Score'], name))

        # 2. 排序（升序）
        chinese_list.sort()
        math_list.sort()
        english_list.sort()

        # 3. 计算各科数据。解包！！！！！
        # 语文
        ch_min_score, ch_min_name = chinese_list[0]
        ch_max_score, ch_max_name = chinese_list[-1]
        ch_avg = sum(s for s, _ in chinese_list) / len(chinese_list)

        # 数学
        ma_min_score, ma_min_name = math_list[0]
        ma_max_score, ma_max_name = math_list[-1]
        ma_avg = sum(s for s, _ in math_list) / len(math_list)

        # 英语
        en_min_score, en_min_name = english_list[0]
        en_max_score, en_max_name = english_list[-1]
        en_avg = sum(s for s, _ in english_list) / len(english_list)

        # 4. 输出结果
        print("===== 班级成绩统计 =====")
        print(
            f"语文 | 最高分：{ch_max_score}（{ch_max_name}），最低分：{ch_min_score}（{ch_min_name}），平均分：{ch_avg:.2f}")
        print(
            f"数学 | 最高分：{ma_max_score}（{ma_max_name}），最低分：{ma_min_score}（{ma_min_name}），平均分：{ma_avg:.2f}")
        print(
            f"英语 | 最高分：{en_max_score}（{en_max_name}），最低分：{en_min_score}（{en_min_name}），平均分：{en_avg:.2f}")







while True:

    print(menu)
    choice = input("请选择操作：")

    match choice:
        case '1':

            student_name = input("请输入学生信息：")

            stu_add(student_name)

        case '2':

             student_name = input("请输入学生信息：")
             update_stu(student_name)


        case '3':

            student_name = input("请输入学生信息：")
            del_stu(student_name)

        case '4':

            student_name = input("请输入要查询的学生姓名：")
            search_stu(student_name)

        case '5':
            show_all()

        case '6':
            calc_all()

        case '7':
            print("Bye")
            break

        case _:
            print("非法操作不支持！")