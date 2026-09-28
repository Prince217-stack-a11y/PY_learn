# import random as rnd
# random_number = rnd.randint(0, 100)
# guess_count = 0
# while True:
#
#     num = int(input("请输入数字: "))
#     guess_count += 1
#     if num == random_number:
#         print("猜对了！")
#         break
#     elif num > random_number:
#         print("数猜大了")
#     elif num < random_number:
#         print("数猜小了")
# print(f"你一共猜测{guess_count}次")
#
#
# #
#
# print()
# print("##############################")
# print("########欢迎进入BMI计算器########")
# print("##############################")
#
# weg = float(input("请输入你的体重(Kg)："))
# heg = float(input("请输入你的身高(cm)："))
# while weg <= 0 or heg <= 0:
#     print("输入有误，请重新输入")
#     weg = float(input("请输入你的体重(Kg)："))
#     heg = float(input("请输入你的身高(cm)："))
# if weg > 0 and heg > 0:
#     print(f"您的BMI值为：{round((weg/(heg**2))*10000,2)}")
# else:
#     print("输入有误请重新输入")

#死循环例子
#1
# i = 0
# while i < 5:
#     print(i)
# #改正
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
# #2
# #无错误无需改正
# i = 0
# while i < 5:
#     print(i)
#     i += 1




#3
#无错误无需改正
# while True:
#     command = input("输入 quit 退出：")
#
#     if command == "quit":
#         break




# #4
# i = 0
#
# while i < 5:
#     if i == 2:
#         continue
#
#     print(i)
#     i += 1
#改正
# i = 0
# while i < 5:
#     if i == 2:
#         i += 1
#         continue
#     print(i)
#     i += 1

#
#
#
#
#5
i = 0

while i < 3:
    for j in range(5):
        if j == 2:
            break

    print(i)
    i += 1
#无错误无需改正















