Installation
============

The easiest method of getting Ballad is to use PIP.

.. code-block:: console

   $ pip install ballad

If you are a developer, or want those *really* fresh features, you can clone the source.

.. code-block:: console

   $ git clone https://github.com/BD103/Ballad.git
   $ cd Ballad
   $ pip install -r requirements.txt

Dependencies
------------

Ballad has two main dependencies:

* `Click <https://pypi.org/project/click>`_ for easy command-line interfaces
* `Tomlkit <https://pypi.org/project/tomlkit>`_ for reading lockfiles. (This comes with Poetry as well.)
