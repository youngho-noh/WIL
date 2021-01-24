# 2018 January location from travel

import json
from pprint import pprint

# google검색해서 함수 만듬
# 함수 설명 : 리스트 내부에 여러 dictionary가 존재한다
# dictionary를 하나씩 for 문으로 담는다
# 내가 찾는 key가 dictionary에 존재하면
# 해당 dictionary를 'result_list'(list)에 담는다
def get_value_list(listofdict, key):
    result_list = []
    for subVal in listofdict:
        if key in subVal:
            result_list += [subVal]
    return result_list

map_info = open('Takeout/위치 기록/Semantic Location History/2018/2018_JANUARY.json', encoding='utf-8')
dic_map = json.load(map_info)

time_line = dic_map['timelineObjects']

# get_value_list 함수 사용(1번 함수)
place_visit = get_value_list(time_line, 'placeVisit')

# get_value_list 함수 조금 변형
# 리스트 내부 dict를 for문을 통해 하나씩 나눠줌
# 해당 리스트에 내가 원하는 키 값이 있는지 if문을 통해 확인
# (여기는 무조건 있겠지만) 있으면 미리 만들어준 리스트에 하나씩 넣음
location = []
for dict_location in place_visit:
    if 'location' in dict_location['placeVisit']:
        location += [dict_location['placeVisit']]

name = []
for name_location in location:
    if 'name' in name_location['location']:
        name += [name_location['location']]

what_i_want = []
for place_name in name:
    what_i_want += [place_name['name']]


pprint(list(set(what_i_want)))
print(type(what_i_want))


