import json
text = '{"name": "老王", "age": 30, "city": "天津" ,"skills":["pythpn", "Git"], "pssed": true, "remark": null}'
text2py = json.loads(text)

print(text2py)
print(type(text2py))
print(text2py["name"])
print(text2py["skills"][0])
print(text2py["pssed"])
print(text2py["remark"])
print(text2py["age"])
