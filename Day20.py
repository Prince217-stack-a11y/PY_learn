# import os
# from pathlib import Path
# import requests
# from dotenv import load_dotenv

# BASE_DIR = Path(__file__).resolve().parent
# load_dotenv(BASE_DIR / ".env")

# api_key = os.getenv("DEEPSEEK_API_KEY")
# base_url = os.getenv("DEEPSEEK_BASE_URL")

# print("API Key 是否加载：", bool(api_key))
# print("Base URL：", base_url)

from cProfile import label

import requests
import plotly.express as px

url = "https://api.github.com/search/repositories?q=language:python&sort:stars&stars:>10000"

headers = {
    "Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

response_dict = r.json()

repos_links, repos_stars, hover_texts = [], [], []
for repo_dict in response_dict["items"]:
    r_name = repo_dict["name"]
    r_url = repo_dict["html_url"]
    r_link = f"<a href='{r_url}>【{r_name}】</a>"
    r_stars = repo_dict["stargazers_count"]
    r_owner = repo_dict["owner"]["login"]
    r_desc = repo_dict["description"]
    r_hover = f"Owner: {r_owner}<br />Description: {r_desc}"

    repos_links.append(r_link)
    repos_stars.append(r_stars)
    hover_texts.append(r_hover)

title = "Github上Stars数最多的Python项目！"
labels = {"x": "项目", "y": "Stars数"}
fig = px.bar(x=repos_links, y=repos_stars, hover_name=hover_texts, title=title, labels=labels)

fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)
fig.show()
