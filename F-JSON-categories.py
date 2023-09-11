import json
from collections import OrderedDict, defaultdict

inter = int(input())
big_json = []

for _ in range(inter):
    data_lines = []
    cnt_row = int(input())
    for _ in range(cnt_row):
        data_lines.append(input())

    data = json.loads(''.join(data_lines), object_pairs_hook=OrderedDict)

    parent_to_children = defaultdict(list)

    for i in data:
        parent_id = i.get('parent')
        parent_to_children[parent_id].append(i)

    for i in data:
        i['next'] = parent_to_children[i['id']]
        for j in i['next']:
            del j['parent']

    big_json.extend({k: v for k, v in i.items() if k != 'parent'} for i in data if i.get('id') == 0)

output_json = json.dumps(big_json)
print(output_json)