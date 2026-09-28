from typing import Optional
from typing import Tuple
from typing import Union
from typing import List
from typing import Dict
from typing import Iterable
from typing import TypedDict
from dataclasses import dataclass

#案例一

def calc_area(width: int, height: int) -> int:
    return width * height
def calc_perimeter(width, height):
    return 2 * (width + height)
def print_rectangle_report(width: int, height: int) -> None:
    print(f"面积：{calc_area(width, height)}, 周长：{calc_perimeter(width, height)}")




#案例二

scores = [88, 59, 92, 71, 45, 100, 60, 76, 59, 0]

def calc_avg(score: list[int]) -> float:
    return sum(scores)/len(scores)
def get_failed_scores(score:list[int]) -> list[int]:
    failed_stu = []
    for score in scores:
        if score <60:
            failed_stu.append(score)
    return failed_stu
def calc_score(scores:list[int]) -> None:
    avg = calc_avg(scores)
    failed_stu = get_failed_scores(scores)
    print(f"最高分为{max(scores)},最低分为{min(scores)}")
    print(f"平均分为{avg}")
    print(f"不及格成绩为{failed_stu}")


#案例三
#原函数
todos = [
    {"title": "学习函数", "done": False},
    {"title": "完成练习", "done": True},
]
#修改
from typing import TypedDict

class TodoDict(TypedDict):
    title: str
    done: bool

def add_todo(todos:list[TodoDict], title:str) -> bool:
    for todo in todos:
        if todo["title"] == title:
            return False

    todos.append({
        "title": title,
        "done": False,
    })
    return True




def print_todos(todos:list[dict[str,str | bool]]) -> None:
    for todo in todos:
        mark = "[x]" if todo["done"] else "[ ]"
        print(f"{mark} {todo['title']}")




#团队代码
# from __future__ import annotations
#
# import json
# from dataclasses import dataclass, field
# from pathlib import Path
#
#
# PASS_SCORE = 60
#
#
# @dataclass
# class Student:
#     """表示一个学生及其各科成绩。"""
#
#     student_id: str
#     name: str
#     scores: dict[str, int]
#
#     def total_score(self) -> int:
#         """返回所有科目的总分。"""
#         return sum(self.scores.values())
#
#     def average_score(self) -> float:
#         """返回各科平均分。"""
#         if not self.scores:
#             return 0.0
#
#         return self.total_score() / len(self.scores)
#
#     def failed_subjects(self, threshold: int = PASS_SCORE) -> list[str]:
#         """返回低于及格线的科目名称。"""
#         return [
#             subject
#             for subject, score in self.scores.items()
#             if score < threshold
#         ]
#
#     def to_dict(self) -> dict[str, object]:
#         """转换成适合写入 JSON 的普通字典。"""
#         return {
#             "student_id": self.student_id,
#             "name": self.name,
#             "scores": dict(self.scores),
#         }
#
#     @classmethod
#     def from_dict(cls, data: dict[str, object]) -> Student:
#         """从 JSON 读取出来的字典创建 Student。"""
#         student_id = data.get("student_id")
#         name = data.get("name")
#         raw_scores = data.get("scores")
#
#         if not isinstance(student_id, str) or not student_id:
#             raise ValueError("student_id 必须是非空字符串")
#
#         if not isinstance(name, str) or not name:
#             raise ValueError("name 必须是非空字符串")
#
#         if not isinstance(raw_scores, dict):
#             raise ValueError("scores 必须是字典")
#
#         scores: dict[str, int] = {}
#
#         for subject, score in raw_scores.items():
#             if not isinstance(subject, str):
#                 raise ValueError("科目名称必须是字符串")
#
#             if isinstance(score, bool) or not isinstance(score, (int, float)):
#                 raise ValueError(
#                     f"科目 {subject} 的成绩不是数字：{score!r}"
#                 )
#
#             scores[subject] = int(score)
#
#         return cls(
#             student_id=student_id,
#             name=name,
#             scores=scores,
#         )
#
#
# @dataclass
# class GradeBook:
#     """管理一组学生。"""
#
#     students: list[Student] = field(default_factory=list)
#
#     def add_student(self, student: Student) -> None:
#         """添加学生，并检查学号是否重复。"""
#         if self.find_by_id(student.student_id) is not None:
#             raise ValueError(
#                 f"学号 {student.student_id} 已存在"
#             )
#
#         self.students.append(student)
#
#     def find_by_id(self, student_id: str) -> Student | None:
#         """按学号查找学生，找不到时返回 None。"""
#         for student in self.students:
#             if student.student_id == student_id:
#                 return student
#
#         return None
#
#     def remove_student(self, student_id: str) -> bool:
#         """按学号删除学生。"""
#         student = self.find_by_id(student_id)
#
#         if student is None:
#             return False
#
#         self.students.remove(student)
#         return True
#
#     def class_average(self) -> float:
#         """返回全班学生平均分。"""
#         if not self.students:
#             return 0.0
#
#         return (
#             sum(
#                 student.average_score()
#                 for student in self.students
#             )
#             / len(self.students)
#         )
#
#     def failed_students(
#         self,
#         threshold: int = PASS_SCORE,
#     ) -> list[Student]:
#         """返回存在不及格科目的学生。"""
#         return [
#             student
#             for student in self.students
#             if student.failed_subjects(threshold)
#         ]
#
#     def summary(self) -> dict[str, object]:
#         """返回适合展示的统计摘要。"""
#         return {
#             "student_count": len(self.students),
#             "class_average": round(self.class_average(), 2),
#             "failed_student_names": [
#                 student.name
#                 for student in self.failed_students()
#             ],
#         }
#
#
# def load_gradebook(path: Path) -> GradeBook:
#     """从 JSON 文件加载学生数据。"""
#     if not path.exists():
#         return GradeBook()
#
#     try:
#         payload = json.loads(
#             path.read_text(encoding="utf-8")
#         )
#
#     except json.JSONDecodeError as error:
#         raise ValueError(
#             f"JSON 文件格式错误：{path}"
#         ) from error
#
#     if not isinstance(payload, list):
#         raise ValueError("学生数据顶层必须是列表")
#
#     students: list[Student] = []
#
#     for index, item in enumerate(payload, start=1):
#         if not isinstance(item, dict):
#             raise ValueError(
#                 f"第 {index} 条学生数据不是字典"
#             )
#
#         try:
#             student = Student.from_dict(item)
#         except (TypeError, ValueError) as error:
#             raise ValueError(
#                 f"第 {index} 条学生数据无效：{item!r}"
#             ) from error
#
#         students.append(student)
#
#     return GradeBook(students=students)
#
#
# def save_gradebook(path: Path, gradebook: GradeBook) -> None:
#     """把学生数据保存为 JSON 文件。"""
#     payload = [
#         student.to_dict()
#         for student in gradebook.students
#     ]
#
#     text = json.dumps(
#         payload,
#         ensure_ascii=False,
#         indent=2,
#     )
#
#     path.write_text(
#         text + "\n",
#         encoding="utf-8",
#     )
#
#
# def format_student(student: Student) -> str:
#     """格式化单个学生的信息。"""
#     failed_subjects = student.failed_subjects()
#     failed_text = (
#         "、".join(failed_subjects)
#         if failed_subjects
#         else "无"
#     )
#
#     return (
#         f"{student.student_id} "
#         f"{student.name} | "
#         f"总分：{student.total_score()} | "
#         f"平均分：{student.average_score():.2f} | "
#         f"不及格科目：{failed_text}"
#     )
#
#
# def print_report(gradebook: GradeBook) -> None:
#     """输出班级报告。"""
#     print("=" * 60)
#     print("学生成绩报告")
#     print("=" * 60)
#
#     if not gradebook.students:
#         print("暂无学生数据")
#         print("=" * 60)
#         return
#
#     for student in gradebook.students:
#         print(format_student(student))
#
#     summary = gradebook.summary()
#
#     print("-" * 60)
#     print(f"学生人数：{summary['student_count']}")
#     print(f"班级平均分：{summary['class_average']:.2f}")
#
#     failed_names = summary["failed_student_names"]
#
#     if failed_names:
#         print(f"存在不及格科目的学生：{failed_names}")
#     else:
#         print("所有学生均已及格")
#
#     print("=" * 60)
#
#
# def main() -> None:
#     """程序入口。"""
#     gradebook = GradeBook()
#
#     gradebook.add_student(
#         Student(
#             student_id="S001",
#             name="小明",
#             scores={
#                 "Python": 88,
#                 "数学": 76,
#                 "英语": 90,
#             },
#         )
#     )
#
#     gradebook.add_student(
#         Student(
#             student_id="S002",
#             name="小红",
#             scores={
#                 "Python": 59,
#                 "数学": 92,
#                 "英语": 85,
#             },
#         )
#     )
#
#     gradebook.add_student(
#         Student(
#             student_id="S003",
#             name="小刚",
#             scores={
#                 "Python": 76,
#                 "数学": 81,
#                 "英语": 78,
#             },
#         )
#     )
#
#     print_report(gradebook)
#
#     output_path = Path(__file__).with_name("students.json")
#     save_gradebook(output_path, gradebook)
#
#     loaded_gradebook = load_gradebook(output_path)
#
#     print("\n重新读取文件后的报告：")
#     print_report(loaded_gradebook)
#
#
# if __name__ == "__main__":
#     main()