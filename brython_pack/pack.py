import os

import brython_pack.utils as utils


class Pack:

    def __init__(self):
        self.bob = {}
        self.dependencies = {}
        self.modules = set()

    def work(self, path_file):
        if os.path.isfile(path_file):
            self.__process(path_file)
        else:
            self.__process_dir(path_file)

    def __process_dir(self, path):
        for f in utils.walk(path):
            self.__process(f.path)

    def __process(self, afile):
        key = afile.replace('/', '.')
        key = key[:-3]
        with open(afile, 'r') as pyf:
            content = '\n'.join(utils.filter_out_docstring(pyf.read()))
            if '__init__' in key:
                key = key.replace('.__init__', '')
                self.bob[key] = ['.py', content, 1]
            else:
                self.bob[key] = ['.py', content]
