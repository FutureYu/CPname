import json
from xpinyin import Pinyin 

with open("data/idiom.json", encoding='utf-8') as f:
    idioms = json.loads(f.read())

with open("data/ci.json", encoding='utf-8') as f:
    cis = json.loads(f.read())

p = Pinyin() 

# 从成语中加入数据库
newIdioms = []
for idiom in idioms:
    newIdioms.append({"word": idiom["word"], "pinyin": set(p.get_pinyin(idiom["word"],' ').split())})

# 从词语中加入数据库
# for ci in cis:
#     newIdioms.append({"word": ci["ci"], "pinyin": set(p.get_pinyin(ci["ci"],' ').split())})


name1 = input("name1: ")
name2 = input("name2: ")


namePinyin1 = p.get_pinyin(name1,' ').split()
namePinyin2 = p.get_pinyin(name2,' ').split()
for name in [{x,y} for x in namePinyin1 for y in namePinyin2]:
    print(name)
    for idiom in newIdioms:
        if name.issubset(idiom["pinyin"]):
            print(idiom["word"])
