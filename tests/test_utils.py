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


def test_filter_docstring():
    matrix = [
        '""" single line """',
        '     """ single line variant """',
        '   """ multiple \n line \n doc string\n """',
        '  """ multiline\n doc \n string\n """',
    ]
    for test in matrix:
        result = list(utils.filter_out_docstring(test))
        assert len(result) == 0
