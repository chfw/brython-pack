================================================================================
brython-pack - Pack up your python package for Brython.js
================================================================================

.. image:: https://api.travis-ci.org/chfw/brython-pack.svg?branch=master
   :target: http://travis-ci.org/chfw/brython-pack

.. image:: https://codecov.io/gh/chfw/brython-pack/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/chfw/brython-pack


Introduction
================================================================================

**brython-pack** packages your Python packages/files into a brython_modules.js. The output is a `brython_modules.js`_ in your
current directory.

.. _brython_modules.js: https://github.com/chfw/bryecharts/tree/master/public/js

Installation
================================================================================


.. code-block:: bash

    $ git clone http://github.com/chfw/brython-pack.git
    $ cd brython-pack
    $ python setup.py install

Usage
================================================================================

::

   usage:
   
       bp brython_stdlib.js requirements.txt your packages and file list
   
   where:
   
       brython_stdlib.js: should be the accessible path to the lib file.
       requirements.txt: is the hard coded and manually worked out dependencies
                         on brython_stdlib.txt. Not the pip requirements.txt.
       your packages file list: could be given as space separated arguments.
   
   examples:
   
       bp dependencies/brython_stdlib.js requirements.txt pyecharts editor.py
