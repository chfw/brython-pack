# -*- coding: utf-8 -*-
DESCRIPTION = (
    'packages your Python packages/files into a brython_modules.js' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'brython-pack'
copyright = u'2017 C.W.'
version = '0.0.0'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'brython-packdoc'
latex_elements = {}
latex_documents = [
    ('index', 'brython-pack.tex',
     'brython-pack Documentation',
     'C.W.', 'manual'),
]
man_pages = [
    ('index', 'brython-pack',
     'brython-pack Documentation',
     [u'C.W.'], 1)
]
texinfo_documents = [
    ('index', 'brython-pack',
     'brython-pack Documentation',
     'C.W.', 'brython-pack',
     DESCRIPTION,
     'Miscellaneous'),
]
