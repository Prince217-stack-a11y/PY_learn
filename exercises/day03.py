print("欢迎进入迷你计算器")
# num1 = float(input("请输入第一个数："))
# num2 = float(input("请输入第二个数："))
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
print(f"a+b={num1+num2}\na-b={num1-num2}\naxb={num1*num2}")
if num2 != 0:
    print(f"a/b = {num1/num2}")
else:
    print("除数不能为0")
