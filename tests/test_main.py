import os
import sys
from mock import patch
from brython_pack.main import main, pack_up, cherry_pick_lib
from nose.tools import raises, eq_


@raises(SystemExit)
def test_0_args():
    with patch.object(sys, "argv", [1]):
        main()


@raises(SystemExit)
def test_help_args():
    with patch.object(sys, "argv", ["-h"]):
        main()


@raises(SystemExit)
def test_three_args():
    with patch.object(sys, "argv", [1, 2, 3]):
        main()


def test_pack_up():
    pathes = [os.path.join("tests", "fixtures", "testproj")]
    expected = {
        "testproj.main": [".py", 'def main():\n    print("Hello World")\n'],
        "testproj": [".py", "", 1],
    }
    ret = pack_up(pathes)
    eq_(expected, ret)


def test_cherry_pick_lib():
    stdlib_path = os.path.join("tests", "fixtures", "brython_stdlib_dummy.js")
    req_file = os.path.join("tests", "fixtures", "bp-requirements.txt")
    stdlib = cherry_pick_lib(stdlib_path, req_file)
    expected = {"testjs": [".js", 'console.log("hello world");']}
    eq_(expected, stdlib)
