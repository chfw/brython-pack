import os
from nose.tools import eq_
from brython_pack.pack import Pack


def test_pack():
    p = Pack()
    p.work(os.path.join("tests", "fixtures", "testproj"))
    expected = {
        "testproj.main": [".py", 'def main():\n    print("Hello World")\n'],
        "testproj": [".py", "", 1],
    }
    eq_(expected, p.bob)


def test_pack_single_file():
    test_file = "test.py"
    with open(test_file, "w") as f:
        f.write("hello single file")
    p = Pack()
    p.work(test_file)
    expected = {"test": [".py", "hello single file"]}
    eq_(expected, p.bob)
    os.unlink(test_file)
