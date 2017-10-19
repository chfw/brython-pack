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
    if len(sys.argv) == 1:
        show_help()

    if sys.argv[1] in ['-h', '--help']:
        show_help()

    if len(sys.argv) < 4:
        print("Nothing to do")
        show_help()

    process(sys.argv[1], sys.argv[2], sys.argv[3:])


def process(lib_file, req_file, packages_and_files):
    # real work:
    std_deps = cherry_pick_lib(lib_file, req_file)
    pack = pack_up(packages_and_files)
    # merge all
    std_deps.update(pack)
    make_brython_modules(std_deps)


def cherry_pick_lib(lib_file, req_file):
    stdlib = StdLib(lib_file)
    with open(req_file, 'r') as f:
        deps = [x for x in f.read().split('\n') if x]
    std_deps = stdlib.install_requires(deps)
    return std_deps


def pack_up(packages_and_files):
    pack = Pack()
    for path in packages_and_files:
        pack.work(path)
    return pack.bob


def show_help():
    print(HELP_TEXT)
    sys.exit(0)


if __name__ == '__main__':
    main()
