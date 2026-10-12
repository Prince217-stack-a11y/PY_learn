import json
from pathlib import Path

output_path = Path(__file__).with_name("student_example.json")

student = {"name": "王子", "scores": [100, 1000, 10000]}

with output_path.open("w", encoding="utf-8") as file:
    json.dump(student, file, ensure_ascii=False, indent=3)#json.dump() -> 写入文件

with output_path.open("r", encoding="utf-8") as file:
    loaded_student = json.load(file)#json.load() -> 从文件读取

print(loaded_student)
print(type(loaded_student))
print(loaded_student["scores"])
