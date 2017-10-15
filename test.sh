pip freeze
nosetests --with-coverage --cover-package brython-pack --cover-package tests  tests docs/source brython-pack && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
