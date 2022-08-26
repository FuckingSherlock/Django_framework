# import json
# from urllib.parse import urljoin

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.zakon.kz/news/"

# with open("Django_framework/templates/link.txt", "w"):
#     pass
# r = requests.get(url)

# if r.ok:  # 200  ## 403 404
#     # print(r.status_code)
#     soup = BeautifulSoup(r.text, "lxml")
#     titles = soup.find("div", class_="z-col-lg-9 z-col-md-9").text
#     link_containers = soup.findAll(
#         "div", {"class": "zmainCard_item card_md z-col-lg-3 z-col-md-3"})
#     # print(titles)
#     counter = 0
#     links_list = []
#     for link_container in link_containers:
#         a_tag = link_container.find("a")
#         if a_tag:
#             link = a_tag.get("href")
#             if urljoin(url, link) not in links_list:
#                 links_list.append(urljoin(url, link))
#         else:
#             counter += 1
#     # print(f"Ошибок нашлось {counter}")

# titl_time = titles.replace("\n", "_")[42:].replace(
#     "_" * 11, "_").replace("__", "_").split("_")[:46]
# # print(titles)

# titles = titl_time[::2]
# times = titl_time[1::2]

# descripts = []
# for i in links_list:
#     r = requests.get(i)
#     if r.ok:
#         soup = BeautifulSoup(r.text, "lxml")
#         descripts.append(soup.find("div", class_="description").text.replace(
#             "\n" + " " * 24, "").replace("    ", ""))
# # print(descripts)

# data = []


# count = 0
# for i in range(0, len(links_list)):
#     data.append({"title": titles[i], "time": times[i],
#                 "descr": descripts[i], "link": links_list[i]})
#     # data[str(titles[i])] = [descripts[count], link.replace('\n', ''), str(titles[i+1])]
#     count += 1
#     if count > 20:
#         break
# # print(data)

# with open("Django_framework/templates/news.json", "w") as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)
