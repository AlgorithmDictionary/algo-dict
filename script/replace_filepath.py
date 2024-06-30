import os

from_path = '../algo_list'

for a_z in os.listdir(from_path):
    folder = os.path.join(from_path, a_z)
    if os.path.isdir(folder):
        for fun_name in os.listdir(folder):
            path = os.path.join(folder, fun_name)
            if not os.path.isdir(path):
                f = path.replace(".md", "")
                if not os.path.exists(f):
                    os.mkdir(f)

                path_new = os.path.join(f, fun_name)
                os.rename(path, path_new)
