================================================================================
brython-pack - Pack up your python package for Brython.js
================================================================================

.. image:: https://api.travis-ci.org/chfw/brython-pack.svg
   :target: http://travis-ci.org/chfw/brython-pack

.. image:: https://codecov.io/github/chfw/brython-pack/coverage.png
   :target: https://codecov.io/github/chfw/brython-pack



Introduction
================================================================================

**brython-pack** packages your Python packages/files into a brython_modules.js. The output is a `brython_modules.js`_ in your
current directory. It is used to pack up `pyecharts.js`_

.. _brython_modules.js: https://github.com/chfw/pyecharts.js/tree/master/public/js
.. _pyecharts.js: https://chfw.github.io/pyecharts.js


Installation
================================================================================


You can install brython-pack via pip:

.. code-block:: bash

    $ pip install brython-pack


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/chfw/brython-pack.git
    $ cd brython-pack
    $ python setup.py install

Limitation
================================================================================

It cannot find the `requirements.txt` file for you, which you need to figure it
out by yourself. Once you will have the dependency list(the dependency on
brython_stdlib.js), the packing step is straight foward.

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
