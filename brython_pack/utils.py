import re
import os
import json


def make_brython_modules(vfs):
    # save in brython_modules.js
    with open("brython_modules.js", "w", encoding="utf-8") as out:
        out.write("__BRYTHON__.use_VFS = true\n__BRYTHON__.VFS = ")
        json.dump(vfs, out)
    # save in brython_modules.js
    with open("brython_modules.log.txt", "w", encoding="utf-8") as out:
        for key in sorted(list(vfs.keys())):
            line = "%s%s(%s)" % (key, vfs[key][0],
                                 'module' if len(vfs[key]) == 3 else 'file')
            out.write("====%s start====\n" % line)
            out.write(vfs[key][1])
            out.write("====%s end====\n\n" % line)


def remove_useless_newlines(src):
    return re.sub('\n(\s+\n)+', '\n\n', src)


def filter_out_docstring(content):
    comment = 0
    triple_in_function = 0
    for line in content.split('\n'):
        if re.match('\s*#', line):
            continue
        if re.match('\s*"{3}.*"{3}', line):
            continue
        if re.match('.*?\S+.*?"{3}', line) and triple_in_function == 0:
            triple_in_function = 1
        if re.match('\s*r?"{3}', line) and comment == 0:
            if triple_in_function == 1:
                triple_in_function == 0
            else:
                comment = 1
                continue
        if re.match('\s*"{3}\s*$', line) and comment == 1:
            comment = 0
            continue
        if comment == 0:
            yield line


def walk(folder):
    for f in os.scandir(folder):
        if f.is_file() and f.path.endswith('.py'):
            yield f
        elif f.is_dir():
            yield from walk(f.path)
