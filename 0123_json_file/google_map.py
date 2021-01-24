# 이전 google map에 저장되어 있던 위치명
# 조만간 지금 google map에 옮겨 넣자!!
# 추후 개선 점 : 이 위치들을 자동으로 google map에 저장할 수 있도록 만들자!

import json
from pprint import pprint

map_info = open('Takeout/지도(내 장소)/저장한 장소.json', encoding='utf-8')
dict_map = json.load(map_info)

location_title = []
for find_title in dict_map['features']:
    location_title.append(find_title['properties']['Title'])
    

for i in location_title:
    print(i)





