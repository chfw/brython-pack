isort $(find brython_pack -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 brython_pack
black -l 79 tests
