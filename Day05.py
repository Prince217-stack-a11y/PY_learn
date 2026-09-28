scores = [88, 59, 92, 71, 45, 100, 60, 76, 59, 0]
scores.sort()
print(scores)
print()

scores_1 = scores[1]
print(scores_1)
scores_2 = scores[5]
print(scores_2)
print()

scores_3 = scores[2: 7: 1]
print(scores_3)
print()
#改动了
scores.append(100)
print(scores)
print()

scores.insert(2,99)
print(scores)
print()

scores.remove(100)
print(scores)
print()

remove_num = scores.pop(0)
print(remove_num)
print()


for index, ascore in enumerate(scores, start=1):
    print(f"{index}: {ascore}")

#实际使用中修改后list和统计分开
print(f"成绩平均分为：{sum(scores)/len(scores)}")
print(f"最高分为：{max(scores)}")
total = 0
for i in scores:
    if i < 60:
        total += 1
print(f"不及格人数为：{total}")
passed_scores = [bscore for bscore in scores if bscore >= 60]
print(passed_scores)



