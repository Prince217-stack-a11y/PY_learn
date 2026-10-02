import json
student = {"name": "老王", "age": 30, "city": "天津" ,"skills":["pythpn", "Git"], "pssed": True, "remark": None}

stu2json = json.dumps(student, ensure_ascii=False, indent=3)
print(stu2json)
print(type(stu2json))


