# 2018 January location from travel

import json
from pprint import pprint

def get_value_list(listofdict, key):
    result_list = []
    for subVal in listofdict:
        if key in subVal:
            result_list += [subVal]
    return result_list

map_info = open('Takeout/위치 기록/Semantic Location History/2018/2018_JANUARY.json', encoding='utf-8')
dic_map = json.load(map_info)

time_line = dic_map['timelineObjects']

place_visit = get_value_list(time_line, 'placeVisit')

location = []
for dict_location in place_visit:
    if 'location' in dict_location['placeVisit']:
        location += [dict_location['placeVisit']]

#여기서 부터 조금 다름!!

