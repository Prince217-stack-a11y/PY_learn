# import os
#
# print(os.getcwdu())       # 当前工作目录
# print(os.listdir())      # 列出目录内容
# print(os.getenv("PATH")) # 获取环境变量
#
# import time
#
# print(time.time())       # 当前时间戳
# time.sleep(2)            # 暂停 2 秒

# import json
#
# data = {
#     "name": "小明",
#     "score": 88,
# }
#
# text = json.dumps(data, ensure_ascii=False)
# print(text)


# import json
#
# data = {'key1' : 'value1', 'key2' : 'value2'}
# json_data = json.dumps(data)
# print(json_data)

# import time
#
# print(time.time())

# import sys
# argu = sys.argv
# print(argu)


# import os
#
# print(dir(os))

#pip 用法
# 1.pip install 库名
# 2.pip install 库名 -i 镜像源
# 3.pip install 库文件 （.whl）




import json
import os
import random
import time

students = ["小明", "小红", "小刚", "小丽", "小丽", "小红"]

selected_stu = random.sample(students, 3)
selected_stu_final = set(selected_stu)
print("抽取结果：", selected_stu_final)



start = time.perf_counter()
data = {"students": selected_stu, "directory": os.getcwd(),}
text = json.dumps(data, ensure_ascii=False, indent=2)
print(text)
end = time.perf_counter()

print(f"运行时间：{end - start:.6f} 秒")
