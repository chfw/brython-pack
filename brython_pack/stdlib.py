import json

import brython_pack.utils as utils


class StdLib:
    def __init__(self, lib_path):
        self.stdlib = None
        with open(lib_path, encoding="utf-8") as fobj:
            modules = fobj.read()
            modules = modules[modules.find('{'):]
            self.stdlib = json.loads(modules)

    def install_requires(self, modules):
        """Build brython_modules.js from the list of modules needed by the
        application.
        """
        vfs = {}
        for module in modules:
            if module in self.stdlib:
                vfs[module] = self.stdlib[module]
                src = vfs[module][1]
                if vfs[module][0] == '.py':
                    src = '\n'.join(list(utils.filter_out_docstring(src)))
                src = utils.remove_useless_newlines(src)
                vfs[module][1] = src
            else:
                print("%s is not found" % module)
        return vfs
