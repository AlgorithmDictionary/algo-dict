# coding=utf-8

class FileProperties(object):

    fun_name = None
    file_path = None
    tag = []
    title = None
    prop = {}

    def __init__(self, file_path, fun_name):
        self.file_path = file_path
        self.fun_name = fun_name
        current_t = None
        current_body = []
        with open(file_path) as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                if line.startswith('# '):
                    self.title = line.replace('# ', '')
                    continue
                if line.startswith('## '):
                    if current_t is not None:
                        self.prop[current_t] = current_body
                        current_body = []
                    # first h2
                    current_t = line.replace('## ', '')
                else:
                    current_body.append(line)
            # last h2
            if current_t is not None:
                self.prop[current_t] = current_body





