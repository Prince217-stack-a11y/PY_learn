# PY_learn

学习过程中写的 Python 练习、智能体笔记和一些小工具都放在这个仓库里，按用途分了目录，方便翻看和整理。

## 目录结构

- `exercises/`：每天跟着学习计划写的练习，统一用 dayNN 命名（按学习计划的天数编号），练习用到的样例数据（todo.json、sample.log 等）放在脚本旁边，因为代码里是按脚本所在位置读取的。
- `notes/agent/`：智能体学习阶段的笔记和观察记录（day22 之后的 md 都归在这里）。
- `projects/`：成块的练习项目，一个项目一个文件夹：
  - `day17_json/`：JSON 持久化待办练习
  - `day21_deepseek/`：调用大模型接口的命令行对话练习
  - `day24a_todowrite/`：TodoWrite 练习
  - `module/`：模块导入练习
- `materials/`：交付材料类文档。
- `_sandbox/`：随手写的一次性脚本，隔段时间清理一次。

## 整理思路

之前所有文件都平铺在根目录，练习代码、笔记和临时文件混在一起，找东西只能靠记文件名。这次整理按「之后还会不会用到」把东西分成四类：

1. 每天练习：进 `exercises/`，统一成 dayNN 命名，和计划天数对应；
2. 成块的练习：进 `projects/`，一个文件夹一个项目，可以整个拷走；
3. 笔记和材料：分别进 `notes/` 和 `materials/`；
4. 一次性脚本、测试输出：进 `_sandbox/`，确认没用的直接删。

根目录只留和仓库本身有关的东西（README、requirements、.gitignore）。另外有几个数据文件必须和对应脚本放在同一个目录（todo.json、sample.log、student_example.json、todo_example.json），因为代码里是按脚本位置读取的，整理时没有拆开它们。

## 运行方式

- 环境：Python 3.13，依赖见 requirements.txt；
- 要用到密钥的练习，把配置写在根目录的 .env 里（.env 不进版本库）。