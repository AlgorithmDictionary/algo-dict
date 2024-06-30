import os

from_path = '../algo_list'

for a_z in os.listdir(from_path):
    folder = os.path.join(from_path, a_z)
    if os.path.isdir(folder):
        for fun_name in os.listdir(folder):
            path = os.path.join(folder, fun_name)
            path_new = os.path.join(folder, fun_name.replace(" ", "_"))
            if path != path_new:
                print(path_new, path)
                os.rename(path, path_new)
