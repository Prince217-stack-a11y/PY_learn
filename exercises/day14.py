# 1.添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
# 1.1输入学生姓名、语文成绩、数学成绩、英语成绩
# 1.2检查学生姓名是否已存在，如果学生不存在，再添加(存在则，不添加)
# 1.3 验证成绩范围(0-100分)
# 1.4 创建学生对象并添加到系统
# 2.修改学生成绩:根据输入的学生姓名，修改对应的学生成绩
# 2.1输入要修改的学生姓名
# 2.2 根据姓名查找该学生，显示该生当前成绩信息
# 2.3 输入新的语文、数学、英语成绩
# 2.4更新学生成绩数据
# 3.删除学生成绩:根据输入的学生姓名，删除对应的学生成绩
# 4.查询指定学生成绩:根据输入的学生姓名，查找对应的学生成绩，并输出
# 4.1输出格式为:“姓名:张三|语文:85 |数学:90 |英语:88|总分:263"
# 5.展示全部学生成绩:展示出系统中所有学生的成绩

#学生类
class Student :

    def __init__(self,name,ch_score,ma_score,en_score) :
        self.name = name
        self.chscore = ch_score
        self.mascore = ma_score
        self.enscore = en_score

    def __str__(self) :
        return f"姓名：{self.name}| 语文：{self.chscore}| 数学：{self.mascore}| 英语：{self.enscore}| 总分：{self.chscore + self.mascore + self.enscore}"

    #修改成绩
    def update_score(self,ch_score=None,ma_score=None,en_score=None) :#有默认值，就可以每次就修改一个或者两个
        if ch_score is not None :
            self.chscore = ch_score
        if ma_score is not None :
            self.mascore = ma_score
        if en_score is not None :
            self.enscore = en_score


#教务管理系统类
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self) :
        self.student_list = []#列表，记录在校学生的成绩信息

    #添加学生成绩
    def add_student(self) :
        name = input("请输入学生的姓名：")
        #判断是否存在
        for s in self.student_list :
            if s.name == name :
                print("该学生已经存在，添加失败！")
                return#代码走到这里结束

        chinese = int(input("请输入学生的语文成绩："))
        math = int(input("请输入学生的数学成绩："))
        english = int(input("请输入学生的英语成绩："))

        #判断分数是否在0-100之间
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100 :
            stu = Student(name, chinese, math, english)#构建对象
            self.student_list.append(stu)
            print("学生信息添加成功！")
        else :
            print("重新操作")


    #修改学生成绩
    def update_student(self) :
        name = input("请输入要修改的学生的姓名：")
        #判断在不在
        for s in self.student_list :
            if s.name == name :
                print(f"当前成绩是：{s}")#是调用__str__

                chinese = int(input("请输入修改后的学生的语文成绩："))
                math = int(input("请输入修改后的学生的数学成绩："))
                english = int(input("请输入修改后的学生的英语成绩："))

                # 判断分数是否在0-100之间
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print("修改成功")
                    print(f"修改后成绩是：{s}")
                    return
                else:
                    print("重新操作")
                    return
        print("未找到该学生，修改失败！")


    #删除学生成绩
    def delete_student(self) :
        name = input("请输入要删除的学生的姓名：")

        for s in self.student_list :
            if s.name == name :
                self.student_list.remove(s)
                print("学生信息删除成功！")
                return
        print("未找到该学生，删除失败！")


    #查询学生成绩
    def query_student(self) :
        name = input("请输入要查询的学生的姓名：")

        for s in self.student_list:
            if s.name == name:
                print(f"学生信息:{s}")
                return
        print("未找到该学生！")


    #展示全部学生成绩
    def list_student(self) :
        for s in self.student_list :
            print(s)


    #运行系统的方法
    def run(self):
        print(f"欢迎使用教务管理系统 {EduManagement.system_version}")

        while True:
             print()
             print("########################################################################")
             print("# 1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生   6.退出系统 #")
             print("#########################################################################")


             choice = input("\n请选择要执行的操作，输入1-6:")
             match choice :
                 case "1" :
                     self.add_student()
                 case "2" :
                     self.update_student()
                 case "3" :
                     self.delete_student()
                 case "4" :
                     self.query_student()
                 case "5" :
                     self.list_student()
                 case "6" :
                     print("Bye!")
                     break
                 case _ :
                     print("输入错误！")


#测试代码
if __name__ == "__main__":

    # 实例
    s1 = Student("王强", 88, 76, 100)
    s2 = Student("王海", 95, 89, 92)
    s3 = Student("王涛", 59, 60, 45)

    print("=== 三个学生成绩 ===")
    print(s1)
    print(s2)
    print(s3)

    print()
    if s1 is s2:
        print("s1 和 s2 是同一个实例")
    else:
        print("s1 和 s2 不是同一个实例")

    # print()
    # print("### 修改王涛的成绩 ###")
    # s3.update_score(ch_score=60, ma_score=20)
    # print(s3)


    edu_management = EduManagement()#调用__init__
    edu_management.student_list.append(s1)
    edu_management.student_list.append(s2)
    edu_management.student_list.append(s3)
    edu_management.run()


