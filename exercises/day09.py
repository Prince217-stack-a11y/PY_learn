# tuple_1 = (1,2,3,4,5,6,7,8,9,10,11,12,13)
#
# print(tuple_1.index(3))
# x,*y,z = tuple_1
#
# print(f"{x},{y},{z}")
#
# a = 10
# b = 20
# a, b = b, a
# print(f"{a},{b}")

# a = [1,2,3]
# # b= a.copy()
# # b = list(a)
# b = a[:]
# b.append(4)
# print(a)
# print(b)

# a = [1, 2, 3]
# b = a
# b.append(4)
#
# print(a)
# print(b)
# print(a is b)
# c = a.copy()
# c.append(5)
#
# print(a)
# print(c)
# print(a is c)
# b = [7, 8, 9]
#
# print(a)
# print(b)
# print(a is b)
# nested_a = [[1, 2], [3, 4]]
# nested_b = nested_a.copy()
#
# nested_b[0].append(99)
#
# print(nested_a)
# print(nested_b)

names = ["小明", "小红", "小刚", "小丽", "小华"]
scores = [88, 59, 76, 92, 45]

stu_list = [(name, score) for name, score in zip(names, scores)]
print(stu_list)
stu_list = [(name, score) for name, score in zip(names, scores) if score >= 60]
print(stu_list)

stu_dict = dict(zip(names, scores))
for name, score in stu_dict.items():
    print(f"姓名：{name},分数：{score}")
