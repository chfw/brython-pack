import os
from nose.tools import eq_
from brython_pack.pack import Pack


def test_pack():
    p = Pack()
    p.work(os.path.join("tests", "fixtures", "testproj"))
    expected = {
        'testproj.main': ['.py', 'def main():\n    print("Hello World")\n'],
        'testproj': ['.py', '', 1]
    }
    eq_(expected, p.bob)
