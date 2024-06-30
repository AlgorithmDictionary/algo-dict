# coding=utf-8

import os
from file_analyse import FileProperties
from xpinyin import Pinyin

p = Pinyin()
from_path = '../algo_list'

target_file =  '../output/TMP_GEN_pinyin_README.MD'
file_header="""
# 算法字典-拼音排序

"""

bodys=[file_header]

pin_map = {}

for a_z in sorted(os.listdir(from_path)):
    folder = os.path.join(from_path, a_z)
    if os.path.isdir(folder):

        for fun_name in os.listdir(folder):
            fun_path = os.path.join(folder, fun_name)
            main_file = os.path.join(fun_path, fun_name + ".md")
            print("file_path: " + fun_path, " file:" + main_file)
            file_ana = FileProperties(main_file, fun_name)
            print(file_ana.title, "exist header: ", file_ana.prop)
            if file_ana != None and file_ana.title != None:
                title = p.get_pinyin(file_ana.title)
                title = title.replace("-", "_")
                for char in title:
                    if char.isalpha():
                        first = char.lower()
                        break

                pinyin = pin_map.get(first, {})
                pinyin[title] = '[{}({})](./algo_list/{}/{}/{}.md)'.format(file_ana.title, fun_name, a_z, fun_name,fun_name)
                pin_map[first] = pinyin


for a_z in sorted(pin_map.keys()):
    pinyin = pin_map.get(a_z, {})
    print("folder: " + a_z)
    bodys.append('## ' + a_z)
    bodys.append('\n')
    for title in pinyin.keys():

        bodys.append(pinyin[title])
        bodys.append("\n\n")




with open(target_file, 'w') as f:
    for body in bodys:
        f.writelines(body)
