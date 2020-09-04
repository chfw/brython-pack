import os
import unittest

from nose.tools import eq_

import brython_pack.utils as utils

TEST_MODULE_LOG = """====testjs.js(file) start====
console.log("hello world");====testjs.js(file) end====

====testmodule.py(file) start====
print("hello world")====testmodule.py(file) end====

"""  # noqa

TEST_MODULE_JS = """__BRYTHON__.use_VFS = true
__BRYTHON__.VFS = {"testjs": [".js", "console.log(\"hello world\");"]}"""  # noqa


def test_newline_removal():
    matrix = ["\n\n\n\n", "\n \n\n \n", "\n\n \n \n" "\n\n \n\n\n\n"]
    for test in matrix:
        result = utils.remove_useless_newlines(test)
        eq_(result, "\n")


def test_filter_docstring():
    matrix = [
        '""" single line """',
        '     """ single line variant """',
        '   """ multiple \n line \n doc string\n """',
        '  """ multiline\n doc \n string\n """',
        'r"""File-like objects that read from or.\n"""',
    ]
    for test in matrix:
        result = list(utils.filter_out_docstring(test))
        assert len(result) == 0, result


def test_not_to_filter_code():
    code = '  f. write("""\\/*\n * Secret Labs\' Engine\n */ \n \n """)'
    expected = [
        '  f. write("""\\/*',
        " * Secret Labs' Engine",
        " */ ",
        " ",
        ' """)',
    ]
    result = list(utils.filter_out_docstring(code))
    eq_(expected, result)


class TestMakeModule(unittest.TestCase):
    def tearDown(self):
        os.unlink("brython_modules.js")
        os.unlink("brython_modules.log.txt")

    def test_make_brython_modules_log(self):
        vfs = {
            "testmodule": [".py", 'print("hello world")'],
            "testjs": [".js", 'console.log("hello world");'],
        }
        utils.make_brython_modules(vfs)
        with open("brython_modules.log.txt", "r") as f:
            self.assertMultiLineEqual(TEST_MODULE_LOG, f.read())

    def test_make_brython_modules_js(self):
        vfs = {"testjs": [".js", 'console.log("hello world");']}
        utils.make_brython_modules(vfs)
        with open("brython_modules.js", "r") as f:
            content = f.read()
            assert "testjs" in content


def test_walk():
    file_list = utils.walk(os.path.join("tests", "fixtures"))
    expected = [
        "tests/fixtures/testproj/__init__.py",
        "tests/fixtures/testproj/main.py",
    ]
    eq_(sorted([f.path for f in file_list]), sorted(expected))
