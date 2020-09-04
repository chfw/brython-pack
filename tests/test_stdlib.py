import os

from nose.tools import eq_

from brython_pack.stdlib import StdLib


def test_stdlib():
    dummy_stdlib = os.path.join("tests", "fixtures", "brython_stdlib_dummy.js")
    lib = StdLib(dummy_stdlib)
    modules = ["testmodule", "testjs"]
    vfs = lib.install_requires(modules)

    expected = {
        "testmodule": [".py", 'print("hello world")'],
        "testjs": [".js", 'console.log("hello world");'],
    }
    eq_(expected, vfs)
