#message:发送第二次请求时，不是只发送最后一句话，而是把整个 messages 列表再次发给模型。原因是 LLM 本身没有跨请求的永久记忆


contacts = {
    "张三": "13800000001",
    "李四": "13900000002",
    "王五": "13700000003",
}
#增
contacts["赵四"] = "13822727726"
print(contacts)


print(contacts["张三"])
print(contacts.get("张三"))
print(contacts.get("赵六"))
print(contacts.get("赵六", "未找到"))




#查
# hun_1 = contacts["张三"]
# print(hun_1)
# hun_2 = contacts["李四"]
# print(hun_2)
# hun_3 = contacts["王五"]
# print(hun_3)
# hun_4 = contacts["赵四"]
# print(hun_4)
# hun_1_1 = contacts.get("张三")
# print(hun_1_1)
# hun_2_2 = contacts.get("李四")
# print(hun_2_2)
# hun_3_3 = contacts.get("王五")
# print(hun_3_3)
# all_num = contacts.keys()
# print(all_num)
# all_hun = contacts.values()
# print(all_hun)
# all_msg = contacts.items()
# print(all_msg)
#
#
# #删
# a = contacts.pop("张三")
# print(a)
# print(contacts)
#
# del contacts["李四"]
# print(contacts)
#
# #改
# print(contacts["王五"])
# contacts["王五"] = "13800000001"
# print(contacts)
#
# #遍历
# for name, number in contacts.items():
#     print(f"{name}: {number}")
# for name in contacts.keys():
#     print(f"{name}")
# for number in contacts.values():
#     print(f"{number}")

#查
# search_name = input("请输入查询人名称：")
#
# number = contacts.get(search_name)#search_name为key
#
# if number is None:
#     print("未找到联系人，请重新查询！")
# else:
#     print(number)


