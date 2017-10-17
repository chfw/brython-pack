from nose.tools import eq_
import brython_pack.utils as utils


def test_newline_removal():
    matrix = [
        '\n\n\n\n',
        '\n \n\n \n',
        '\n\n \n \n'
        '\n\n \n\n\n\n'
    ]
    for test in matrix:
        result = utils.remove_useless_newlines(test)
        eq_(result, '\n\n')
