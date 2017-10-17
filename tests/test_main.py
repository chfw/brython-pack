import sys
from mock import patch
from brython_pack.main import main
from nose.tools import raises


@raises(SystemExit)
def test_0_args():
    with patch.object(sys, 'argv', [1]):
        main()


@raises(SystemExit)
def test_help_args():
    with patch.object(sys, 'argv', ['-h']):
        main()


@raises(SystemExit)
def test_three_args():
    with patch.object(sys, 'argv', [1, 2, 3]):
        main()
