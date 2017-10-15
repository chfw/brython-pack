import sys


from brython_pack._version import __version__
from brython_pack.stdlib import StdLib
from brython_pack.pack import Pack
from brython_pack.utils import make_brython_modules


HELP_TEXT = """version: %s
usage:

    bp brython_stdlib.js requirements.txt your packages and file list

where:

    brython_stdlib.js: should be the accessible path to the lib file.
    requirements.txt: is the hard coded and manually worked out dependencies
                      on brython_stdlib.txt. Not the pip requirements.txt.
    your packages file list: could be given as space separated arguments.

examples:

    bp dependencies/brython_stdlib.js requirements.txt pyecharts editor.py
""" % __version__


def main():
    lib_file = sys.argv[1]
    if lib_file in ['-h', '--help']:
        show_help()
    if len(sys.argv) < 4:
        print("Nothing to do")
        show_help()
    req_file = sys.argv[2]
    packages_and_files = sys.argv[3:]

    # real work:
    stdlib = StdLib(lib_file)
    with open(req_file, 'r') as f:
        deps = [x for x in f.read().split('\n') if x]
    std_deps = stdlib.install_requires(deps)
    pack = Pack()
    for path in packages_and_files:
        pack.work(path)
        std_deps.update(pack.bob)
    make_brython_modules(std_deps)


def show_help():
    print(HELP_TEXT)
    sys.exit(0)


if __name__ == '__main__':
    main()
