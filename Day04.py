
s1 = " 2026-09-12-10:36:01 INFO User login successful "
s2 = " 2026-09-12-10:37:45 WARNING Memory usage exceeds 80 percent "
s3 = " 2026-09-12-10:38:12 ERROR Failed to connect to database "

s1_change = s1.split(maxsplit=2)
print(f"这个字符串中I字母的位置为{s1.find("I")}")
print(f"这个字符串中I字母的数量为{s1.count("I")}")
print(s1.upper())
print(s1.replace("INFO","ERROR"))
print(s1[0: 20: 2])
print(s1[: : -1])
print(f"日期 级别 内容 分别为：{s1_change}")
print("|".join(s1_change))
print(s1.strip(' '))
if "A" in s1:
    print("找到了")
else:
    print("没找到")
print()

s2_change = s2.split(maxsplit=2)
print(f"这个字符串中I字母的位置为{s2.find("I")}")
print(f"这个字符串中I字母的数量为{s2.count("I")}")
print(s2.upper())
print(s2.replace("WARNING","ERROR"))
print(s2[0: 20: 2])
print(s2[: : -1])
print(f"日期 级别 内容 分别为：{s2_change}")
print("|".join(s2_change))
print(s2.strip(' '))
if "B" in s2:
    print("找到了")
else:
    print("没找到")
print()

s3_change = s3.split(maxsplit=2)
print(f"这个字符串中F字母的位置为{s3.find("F")}")
print(f"这个字符串中I字母的数量为{s3.count("I")}")
print(s3.upper())
print(s3.replace("ERROR","WARNING"))
print(s3[0: 20: 2])
print(s3[: : -1])
print(f"日期 级别 内容 分别为：{s3_change}")
print("|".join(s3_change))
print(s3.strip(' '))
if "C" in s3:
    print("找到了")
else:
    print("没找到")





