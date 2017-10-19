import os

import brython_pack.utils as utils


class Pack:

    def __init__(self):
        self.bob = {}
        self.dependencies = {}
        self.modules = set()
        self.base_path = None

    def work(self, path_file):
        self.base_path = os.path.dirname(path_file)
        if os.path.isfile(path_file):
            self.__process(path_file)
        else:
            self.__process_dir(path_file)

    def __process_dir(self, path):
        for f in utils.walk(path):
            self.__process(f.path)

    def __process(self, afile):
        module = self.__extract_module_name(afile)
        with open(afile, 'r') as pyf:
            content = '\n'.join(utils.filter_out_docstring(pyf.read()))
            if '__init__' in module:
                module = module.replace('.__init__', '')
                self.bob[module] = ['.py', content, 1]
            else:
                self.bob[module] = ['.py', content]

    def __extract_module_name(self, afile):
        if self.base_path:
            module = afile[len(self.base_path)+1:]
        else:
            module = afile
        module = module.replace('/', '.')
        module = module[:-3]
        return module
