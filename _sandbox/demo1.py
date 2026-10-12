# name = "Wangzi"
# age = 19
# sub = "智能感知工程"
# hub = "python、ai"
# message = "大家好，我是"+name+",""学习的专业是"+sub+",""爱好是"+hub
# print(message)
# a = 100
# b = 200
# c = 300
# d = a
#  = b
#  = c
# c = d
# print(c, a, b)



# -----------
# 字符串格式化
# a = 18
# print(f"你好，{a}")
# from mkl_random.mklrand import length
# from openpyxl.styles.builtins import total
# import math
# from random import choice

# input输入
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"Your name is {name}. Your age is： {age}")
# key = input("请输入密码：")
# act = 10000
# print(f"您的余额为：{act}")
# tak = input("取款金额：")
# print(f"您的余额为:{act - int(tak)}")
#
# a = input("请输入a：")
# b = input("请输入b：")
# c = int(a)+int(b)
# print(f"{c}")

#
# a,b = 1,2
# # print(f"{a} + {b} = {a+b}")
# #
# # print(type(1.11))
# # print(type(2.11))
# # print(type("nihao"))
# print("\"Hello \n \t World\"")
#
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"Hello {name}! You are {age} years old.")
#
# num = input("Enter a number: ")
#
# match num :
#     case 1 if num % 2 == 0 :
#
#         print(num)
#     case 2 if num % 2 == 1 :
#         print(num)
#     case 3|4 if num % 2 == 1 :
#         print(num)

# total = 0
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         total += i
#     i += 1
#     print(f"{total}")



# i = 0#
# # for i in range(1,1101,2):
#
#
#
#
#
#     i += 1
#
#     print(i)

#
#
# long = int(input("请输入长度："))
#
# wide = int(input("请输入款宽度："))
#
# for j in range(wide):
#     for i in range(long):
#         print("*",end="  ")
#
#     print()

#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} x {i} = {j * i}",end=" | ")
#     print()



# while True:
#
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#
#
#
#     if username == "" and password == "":
#
#         print("输入的用户名和密码不能为空！")
#
#         continue
#
#
#     if username == "admin" and password == "666888":
#
#         print("登陆成功！")
#
#
#         break
#
#     elif username == "zhangsan" and password == "123456":
#
#         print("登陆成功！")
#
#
#         break
#
#     elif username == "taoge" and password == "888666":
#
#         print("登陆成功！")
#
#
#         break
#
#
#     else:
#
#
#         print("登陆失败！")
#


#
#
#
# for i in range(5):
#
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#
#     if username == "admin" and password ==  "666888":
#         print("Login Successful")
#         break
#
#     elif username == "zhangsan" and password == "123456":
#         print("Login Successful")
#         break
#
#     elif username == "taoge" and password == "888666":
#         print("Login Successful")
#         break
#
#     else:
#
#         print("Login Failed.")
#
#         continue



# import random
#
# random_number = random.randint(1, 100)
#
# while True:
#
#     num = int(input("请输入数字"))
#
#     if num > random_number:
#
#         print("大了")
#
#     elif num < random_number:
#
#         print("小了")
#
#     else :
#
#         print("恭喜猜对了！")
#
#         break
# #
# total = 0

# for i in range(1,1001):
#
#     if i % 5 == 0:
#         total += i
# print(total)





#
# total = 0
# msg = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
# for i in msg:
#
#     if i == "a":
#         total += 1
# print(total)
#
# s = [1,2,3,4,5,6,7,8,9]
# del s[0],s[1]
# print(s[0],s[1],s[2])
#
# num_list = []
#
# for i in range(10):
#
#     num = int(input("请输入数字："))
#
#     num_list.append(num)
#
#
# num_list.sort()
#
# print(num_list)
#
# print("最小值：",num_list[0])
#
# print(num_list[-1])
#
# print("平均值：",sum(num_list)/len(num_list))
#
#
#
# num_list = [i**2 for i in range(1,21)]
# print(num_list)
#
# for i in range(1,21):
#
#
#
#      num_list.append(i**=2)
#
# print(num_list)
#
#

#
# num_list = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,]
#
# print(set(num_list))
# new_list = [i**2 for i in num_list if i%2==0]
#
#
# print(new_list)
#
#
# List1 =
#
#
#
# num_list = [*]

# shopping_cart = {}
#
# print("欢迎使用购物车管理系统！")
#
# menu = """
# ######购物车系统#######
# #    1.添加购物车     #
# #    2.修改购物车     #
# #    3.删除购物车     #
# #    4.查询购物车     #
# #    5.退出购物车     #
# #####################
# """
# while True:
#
#     print(menu)
#
#     choice = input("请选择操作：")
#     match choice:
#
#         case "1":
#
#             goods_name = input("请输入商品的名称：")
#             goods_price = float(input("请输入商品的价格："))
#             goods_num = int(input("请输入商品的数量："))
#
#             if goods_num in shopping_cart:
#                 print("该商品已存在")
#             else:
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#                 print("已完成！")
#
#         case "2":
#
#             goods_name = input("请输入商品的名称：")
#
#             if goods_name not in shopping_cart:
#                 print("该商品不存在！")
#             else:
#                 shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#                 print("商品修改完毕")
#                 continue
#
#         case "3":
#
#             goods_name = input("请输入商品的名称：")
#
#             if goods_name not in shopping_cart:
#
#                 print("该商品不存在")
#             else:
#
#                 del shopping_cart[goods_name]
#                 print("删除完毕")
#
#         case "4":
#
#             for goods_name in shopping_cart.keys():
#                 goods_info = shopping_cart[goods_name]
#                 print(f"商品名称： {goods_name}， 商品价格：{goods_info['price']}, 商品数量：{goods_info['num']}")
#
#         case "5":
#
#             print("Bye")
#
#             break
#
#         case _:
#
#             print("非法操作不支持！")


# student_group = {}
# menu = """
# ####################################【菜单】#############################################
# # 1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询学生信息 5.列出所有学生 6.统计班级成绩 7.退出系统 #
# #######################################################################################
# """
#
# while True:
#
#     print(menu)
#     choice = input("请选择操作：")
#
#     match choice:
#         case '1':
#
#             student_name = input("请输入学生信息：")
#
#             if student_name in student_group:
#
#                  print("该学生已存在")
#             else:
#                 student_scr_ch = int(input("请输入学生语文成绩："))
#                 student_scr_ma = int(input("请输入学生数学成绩："))
#                 student_scr_en = int(input("请输入学生英语成绩："))
#                 student_group[student_name] = {"Chinese Score": student_scr_ch, "Math Score": student_scr_ma, "English Score": student_scr_en}
#                 print("已完成！")
#
#         case '2':
#
#              student_name = input("请输入学生信息：")
#              if student_name not in student_group :
#                 print("该学生不存在！")
#              else:
#                  student_scr_ch = int(input("请输入学生新语文成绩："))
#                  student_scr_ma = int(input("请输入学生新数学成绩："))
#                  student_scr_en = int(input("请输入学生新英语成绩："))
#                  student_group[student_name] = {"Chinese Score": student_scr_ch, "Math Score": student_scr_ma, "English Score": student_scr_en}
#                  print("修改完毕")
#
#
#         case '3':
#
#             student_name = input("请输入学生信息：")
#             if student_name not in student_group:
#                 print("该学生不存在！")
#             else:
#                 del student_group[student_name]
#                 print("删除完毕")
#
#         case '4':
#
#             student_name = input("请输入要查询的学生姓名：")
#             if student_name in student_group:
#                 info = student_group[student_name]
#                 print(f"{student_group}")
#             else:
#                 print("该学生不存在！")
#
#         case '5':
#
#             if not student_group:
#                 print("暂无学生信息")
#
#             else:
#                 print("===== 所有学生信息 =====")
#                 for name, scores in student_group.items():
#                     print(f"姓名：{name} | 语文：{scores['Chinese Score']} 数学：{scores['Math Score']} 英语：{scores['English Score']}")
#
#         case '6':
#
#             if not student_group:
#                 print("暂无学生数据，无法统计")
#             else:
#                 # 1. 收集所有学生的各科成绩 + 姓名对应关系
#                 chinese_list = []
#                 math_list = []
#                 english_list = []
#                 for name, scores in student_group.items():#按序先把名字赋值给name，再把成绩赋值给scores
#                     chinese_list.append((scores['Chinese Score'], name))
#                     math_list.append((scores['Math Score'], name))
#                     english_list.append((scores['English Score'], name))
#
#                 # 2. 排序（升序）
#                 chinese_list.sort()
#                 math_list.sort()
#                 english_list.sort()
#
#                 # 3. 计算各科数据。解包！！！！！
#                 # 语文
#                 ch_min_score, ch_min_name = chinese_list[0]
#                 ch_max_score, ch_max_name = chinese_list[-1]
#                 ch_avg = sum(s for s, _ in chinese_list) / len(chinese_list)
#
#                 # 数学
#                 ma_min_score, ma_min_name = math_list[0]
#                 ma_max_score, ma_max_name = math_list[-1]
#                 ma_avg = sum(s for s, _ in math_list) / len(math_list)
#
#                 # 英语
#                 en_min_score, en_min_name = english_list[0]
#                 en_max_score, en_max_name = english_list[-1]
#                 en_avg = sum(s for s, _ in english_list) / len(english_list)
#
#                 # 4. 输出结果
#                 print("===== 班级成绩统计 =====")
#                 print(
#                     f"语文 | 最高分：{ch_max_score}（{ch_max_name}），最低分：{ch_min_score}（{ch_min_name}），平均分：{ch_avg:.2f}")
#                 print(
#                     f"数学 | 最高分：{ma_max_score}（{ma_max_name}），最低分：{ma_min_score}（{ma_min_name}），平均分：{ma_avg:.2f}")
#                 print(
#                     f"英语 | 最高分：{en_max_score}（{en_max_name}），最低分：{en_min_score}（{en_min_name}），平均分：{en_avg:.2f}")
#
#         case '7':
#             print("Bye")
#             break
#
#         case _:
#
#             print("非法操作不支持！")









#
# def circle_area(r):
#     """
#
#     :param r:
#     :return:
#     """
#     return math.pi * r**2
# help(circle_area)
# al = circle_area(10)
# print(al)
#
#
#
# def function_a():
#     print("function a before")
#     function_b()
#     print("function a after")
#
# def function_b():
#     print("function b before")
#     function_c()
#     print("function b after")
#
# def function_c():
#     print("function c ")
#
# function_a()
#
# print("函数调用完毕")



# def tranagle_area(w,h):
#     return w*h/2
#
# print("面积为：", tranagle_area(1000,3223))


# def letter_count(s):
#     total = 0
#     for w in s:
#         if w in 'aeiouAEIOU':
#             total += 1
#     return total
#
# print(letter_count("adwhudhowhqihdclkndionwlfnlhflklvajvaiehfkefljvjopqjfewfhefepfqeifednauefhiweef"))




# def calc_score(score_list):
#
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg_s = round(sum(score_list) / len(score_list),1)
#     return max_s , min_s , avg_s
# s_list = [589,666,743,664,580,687,689,675,358]
# max_s, min_s, avg_s = calc_score(s_list)
# print(max_s, min_s, avg_s)

# def score_com(score):
#     if score >= 90:
#         return 'A'
#     elif score >= 75:
#         return 'B'
#     elif score >= 60:
#         return 'C'
#     elif score < 60:
#         return 'D'
# print(score_com(85))
#

# def fu_a(s):
#     if s ==s[::-1]:
#         return True
#     else:
#         return False
# print(fu_a("abcncba"))


# def fuc_b(s1,s2,s3) -> bool:
#     if s1 ==s2 ==s3:
#         print("等边三角形")
#     elif s1 ==s2 !=s3 or s1 ==s3 !=s2 or s3 ==s2 !=s1 and s1 + s2 > s3 and s3 + s2 > s1 and s1 + s3 > s2:
#         print("等腰三角形")
#     elif s1 + s2 > s3 or s3 + s2 > s1 or s3 + s1 > s2:
#         print("普通三角形")
#     else:
#         print("无法构成三角形")
# fuc_b(29379,412,412)
# 用sort（）函数从小到大排序方便看关系！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！




#不定长参数
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min_data, max_data, round(avg_data, 1)
#
# print(calc_data(1534, 2342, 32424))
# print(calc_data(83, 384, 376,399,33,55,39))


# def calc_data(*args, **kwargs):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#
#     if kwargs.get("round") is not None:
#         avg_data = round(avg_data, kwargs.get("round"))
#
#     if kwargs.get("print") is not None:
#         print(f"计算出来的最小值， 最大值，平均值：")
#
#     return min_data, max_data, round(avg_data, 1)
#
#
# print(calc_data(1534, 2342, 32424, 47363, 838, round=3, print=True))
# print(calc_data(83, 384, 376,399,33,55,3))

# def add (x, y):
#     return x + y
#
#
# def subtract (x, y):
#     return x - y
#
# def multiply (x, y):
#     return x * y
#
# def divide (x, y):
#     return x / y
#
#
# add_num = add(1222, 271)
# multiply_num = multiply(7824687782, 2786382)
# divide_num = divide(49278, 2873982)
#
# print(add_num)
# print(multiply_num)
# print(divide_num)






#类
# class Car:
#     pass
#
# c1 = Car()#动态添加属性，不推荐，降低可读性
# c1.color = "red"
# c1.brand = "BWM"
# print(c1.__dict__)
# print(c1.color)


#推荐方法
# class Car:
#     def __init__(self, c_brand, c_price, c_name):
#         self.c_brand = c_brand
#         self.c_price = c_price
#         self.c_name = c_name
#
#
# c1 = Car("red", 50000, "BWM")
# print(c1)
#
# class Car:
#     def __init__(self, brand, name, price) :
#         self.brand = brand
#         self.name = name
#         self.price = price
#
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶。。。")
#     def total_cost(self, discount, rate) :
#         return self.price * discount + self.price * rate
# c1 = Car("BWM", "X5", 50000000)
# total_cost = c1.total_cost(0.9, 0.1)
# print(f"提车总价为：{total_cost:.0f}")
#
# c1.running()





# class Car:
#     def __init__(self, c_color, c_brand, c_price, c_name):
#         self.color = c_color
#         self.c_brand = c_brand
#         self.c_price = c_price
#         self.c_name = c_name
#         print("Car 类型的对象初始化完毕，对象属性已经添加完毕。")
#
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶。。。")
#
#     def total_cost(self, discount, rate=0.1) :
#         total_cost = self.price * discount + self.price * rate
#         return total_cost
#
#     #魔法方法
#     def __str__(self):
#         return f"{self.color} {self.c_brand} {self.c_price} {self.c_name}"
#
#     def __eq__(self, other):
#         return self.color == other.color and self.c_brand == other.c_brand and self.c_price == other.c_price and self.c_name == other.c_name
#
#     def __lt__(self, other):
#         return self.c_price < other.c_price
#
# c1 = Car("白色", "BYD", 18000, "汉")
# print(c1)
#
# c2 = Car("黑色", "BWM", 29001, "宝马")
# print(c2)
#
# print(c1 == c2)
# print(c1 < c2)




#属性
# class Car:
#     #类属性
#     wheel = 4
#     tax_rate = 0.1
#
#     def __init__(self, c_color, c_brand, c_price, c_name):
#         #实例属性
#         self.color = c_color
#         self.brand = c_brand
#         self.price = c_price
#         self.name = c_name
#         print("Car 类型的对象初始化完毕，对象属性已经添加完毕。")
#
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶。。。")
#
#     def total_cost(self, discount, rate=0.1) :
#         total_cost = self.price * discount + self.price * rate
#         return total_cost
#
# c1 = Car("白色", "BYD", 18000, "汉")
# print(c1.brand)
# print(c1.price)
# print(c1.color)
# print(c1.wheel)
#
# c2 = Car("黑色", "BWM", 29001, "宝马")
# print(c2.__dict__)
#
# print(Car.wheel)








#案例
#采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下:
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
# class Student :
#
#     def __init__(self,name,ch_score,ma_score,en_score) :
#         self.name = name
#         self.chscore = ch_score
#         self.mascore = ma_score
#         self.enscore = en_score
#
#     def __str__(self) :
#         return f"姓名：{self.name}| 语文：{self.chscore}| 数学：{self.mascore}| 英语：{self.enscore}| 总分：{self.chscore + self.mascore + self.enscore}"
#
#     #修改成绩
#     def update_score(self,ch_score=None,ma_score=None,en_score=None) :#有默认值，就可以每次就修改一个或者两个
#         if ch_score is not None :
#             self.chscore = ch_score
#         if ma_score is not None :
#             self.mascore = ma_score
#         if en_score is not None :
#             self.enscore = en_score
#
#
# #教务管理系统类
# class EduManagement:
#     system_version = "1.0"
#     system_name = "教务管理系统"
#
#     def __init__(self) :
#         self.student_list = []#列表，记录在校学生的成绩信息
#
#     #添加学生成绩
#     def add_student(self) :
#         name = input("请输入学生的姓名：")
#         #判断是否存在
#         for s in self.student_list :
#             if s.name == name :
#                 print("该学生已经存在，添加失败！")
#                 return#代码走到这里结束
#
#         chinese = int(input("请输入学生的语文成绩："))
#         math = int(input("请输入学生的数学成绩："))
#         english = int(input("请输入学生的英语成绩："))
#
#         #判断分数是否在0-100之间
#         if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100 :
#             stu = Student(name, chinese, math, english)#构建对象
#             self.student_list.append(stu)
#             print("学生信息添加成功！")
#         else :
#             print("重新操作")
#
#
#     #修改学生成绩
#     def update_student(self) :
#         name = input("请输入要修改的学生的姓名：")
#         #判断在不在
#         for s in self.student_list :
#             if s.name == name :
#                 print(f"当前成绩是：{s}")#是调用__str__
#
#                 chinese = int(input("请输入修改后的学生的语文成绩："))
#                 math = int(input("请输入修改后的学生的数学成绩："))
#                 english = int(input("请输入修改后的学生的英语成绩："))
#
#                 # 判断分数是否在0-100之间
#                 if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
#                     s.update_score(chinese, math, english)
#                     print("修改成功")
#                     print(f"修改后成绩是：{s}")
#                     return
#                 else:
#                     print("重新操作")
#                     return
#         print("未找到该学生，修改失败！")
#
#
#     #删除学生成绩
#     def delete_student(self) :
#         name = input("请输入要删除的学生的姓名：")
#
#         for s in self.student_list :
#             if s.name == name :
#                 self.student_list.remove(s)
#                 print("学生信息删除成功！")
#                 return
#         print("未找到该学生，删除失败！")
#
#
#     #查询学生成绩
#     def query_student(self) :
#         name = input("请输入要查询的学生的姓名：")
#
#         for s in self.student_list:
#             if s.name == name:
#                 print(f"学生信息:{s}")
#                 return
#         print("未找到该学生！")
#
#
#     #展示全部学生成绩
#     def list_student(self) :
#         for s in self.student_list :
#             print(s)
#
#
#     #运行系统的方法
#     def run(self):
#         print(f"欢迎使用教务管理系统 {EduManagement.system_version}")
#
#         while True:
#              print()
#              print("########################################################################")
#              print("# 1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生   6.退出系统 #")
#              print("#########################################################################")
#
#
#              choice = input("\n请选择要执行的操作，输入1-6:")
#              match choice :
#                  case "1" :
#                      self.add_student()
#                  case "2" :
#                      self.update_student()
#                  case "3" :
#                      self.delete_student()
#                  case "4" :
#                      self.query_student()
#                  case "5" :
#                      self.list_student()
#                  case "6" :
#                      print("Bye!")
#                      break
#                  case "_" :
#                      print("输入错误！")
#
#
# #测试代码
# if __name__ == "__main__":
#     edu_management = EduManagement()#调用__init__
#     edu_management.run()





#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#自主练习
# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下:
# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入
# 完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商
# 品数量:xxx"。
# 5.退出购物车

# class Goods:
#     def __init__(self,name,price,number):
#         self.name = name
#         self.price = price
#         self.number = number
#
#     #输出格式
#     def __str__(self):
#         return f"商品名称：{self.name} 商品价格：{self.price} 商品数量：{self.number}"
#
#     #修改数量
#     def update_number(self,number=None):
#         if number is not None:
#             self.number = number
#
#
# #购物管理系统
# class ShoppingCart:
#     system_name = "购物管理系统"
#     system_version = "1.0.0"
#
#     def __init__(self):
#         self.goods_list = []
#
#     #添加
#     def add_goods(self):
#         name = input("请输入商品名称：")
#         price = int(input("请输入商品价格："))
#         number = int(input("请输入商品数量："))
#         if 0 <= number and 0 <= price:
#             goods = Goods(name,price,number)
#             self.goods_list.append(goods)
#             print("添加成功！")
#         else :
#             print("请重新操作")
#
# #想加入可以显示已添加该商品多少数量功能
#
#     #修改
#     def update_goods(self):
#         name = input("请输入要修改商品名称：")
#         for i in self.goods_list:
#             if i.name == name:
#                 print(f"当前商品信息为{i}")
#
#
#                 number = int(input("请输入要修改商品数量："))
#
#                 if 0<=number:
#                     i.update_number(number)
#                     print("修改成功!")
#                     print(f"当前商品信息为：{i}")
#                     return
#                 else:
#                     print("重新操作")
#                     return
#
#
#     #删除
#     def delete_goods(self):
#         name = input("请输入要删除商品名称：")
#         for i in self.goods_list:
#             if i.name == name:
#                 self.goods_list.remove(i)
#                 print("删除成功！")
#                 return
#         print("未找到该商品，删除失败！")
#
#
#     #查询
#     def query_goods(self):
#         name = input("请输入要查询商品：")
#         for i in self.goods_list:
#             if i.name == name:
#                 print(f"商品信息为:{i}")
#                 return
#             print("未找到该商品")
#
#
#
#     #展示全部
#     def show_goods(self):
#         for i in self.goods_list:
#             print(i)
#
#     #系统运行
#     def run(self):
#         print(f"欢迎使用购物管理系统： {ShoppingCart.system_version}")
#
#         while True:
#
#             print("\n#################################################################")
#             print("#1.添加购物车 2.修改购物车 3.删除购物车 4.查询购物车 5.查询全部 6.退出购物车#")
#             print("##################################################################")
#
#             choice = input("\n请输入操作，1-6：")
#
#             match choice:
#                 case "1":
#                     self.add_goods()
#                 case "2":
#                     self.update_goods()
#                 case "3":
#                     self.delete_goods()
#                 case "4":
#                     self.query_goods()
#                 case "5":
#                     self.show_goods()
#                 case "6":
#                     print("Bye!")
#                     break
#                 case _:
#                     print("输入有误，请重新操作！")
#
#
# #测试代码
# if __name__ == "__main__":
#     shopping_cart = ShoppingCart()
#     shopping_cart.run()












