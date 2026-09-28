# f1 = open("test.txt", "r", encoding="utf-8")
# content = f1.readlines()
# print(content)
# f = open("test1.txt","w")
# f.write("hello world")
# f.writelines("\n1000000")
# f.close()

# with open("test1.txt","r+") as f:
#     f.read(1000)
#     print(f.readlines())

#
# import pathlib as pl
# f1 = open("pi.txt", "w", encoding="utf-8")
# from pathlib import Path
# path = Path("test1.txt")
# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
# print(path.cwd())
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)


# folder = Path(".")
#
# for item in folder.iterdir():
#     print(item)
# print()
# for item in folder.glob("*.py"):
#     print(item)
# print()
# for item in folder.rglob("*.py"):
#     print(item)

# p = Path(__file__).resolve().parent / "enc_test.txt"
# p.write_text("中文日志：数据库连接失败", encoding="utf-8")
#
# print(p.read_text(encoding="utf-8"))
# print(p.read_text(encoding="gbk"))
# print(p.read_text())













# 1. 总行数
# 2. ERROR 出现次数
# 3. 最长的一行
# 4. 最长行的字符长度
#
# 文件路径：...
# 文件是否存在：True
# 总行数：8
# ERROR 次数：3
# 最长行长度：...
# 最长行内容：...






# f = open("E:\pycharm_ana_envir\PY_learn\sample.log", "r")


from pathlib import Path



def get_log_path():
    script_dir = Path(__file__).resolve().parent
    return script_dir / "sample.log"


def count_lines(path):
    total = 0
    with open(path,"r", encoding="utf-8") as f:
        for line in f:
            total += 1
    return f'总行数为：{total}'


def count_error(path):
    with open(path,"r", encoding="utf-8") as f:
        s = 0
        for line in f:
            s += line.count("ERROR")
        return f"ERROR出现次数为：{s}"




def find_longest_line(path):
    longest =  ""
    with open(path,"r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if len(line) > len(longest):#>比的不是长度是字符串内容
                longest = line
    return f'最长的一行是：{longest}, 长度是：{len(longest)}'





if __name__ == "__main__":
    log_path = get_log_path()
    print(count_lines(log_path))
    print(count_error(log_path))
    print(find_longest_line(log_path))
