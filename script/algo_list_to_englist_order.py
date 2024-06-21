# coding=utf-8

import os
from file_analyse import FileProperties

from_path = '../algo_list'

target_file =  '../output/TMP_GEN_ENG_README.MD'
file_header="""
# 算法字典-英文首字符排序

"""

bodys=[file_header]

for a_z in os.listdir(from_path):
    folder = os.path.join(from_path, a_z)
    if os.path.isdir(folder):
        print("folder: " + a_z)
        bodys.append('## ' + a_z)
        bodys.append('\n')
        for fun_name in os.listdir(folder):
            fun_path = os.path.join(folder, fun_name)
            main_file = os.path.join(fun_path, fun_name + ".md")
            print("file_path: " + fun_path, " file:" + main_file)
            file_ana = FileProperties(main_file, fun_name)
            print(file_ana.title, "exist header: ", file_ana.prop)

            b = ('[{}({})](./algo_list/{}/{}/{}.md)'
                 .format(fun_name, file_ana.title, a_z, fun_name,fun_name))
            bodys.append(b)
            bodys.append("\n\n")

with open(target_file, 'w') as f:
    for body in bodys:
        f.writelines(body)