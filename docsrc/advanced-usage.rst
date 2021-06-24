Advanced Usage
==============

.. warning:: 
   This page is a work in progress!

.. note:: 
   For when you want to fine tune the process or edit the core installer. It is recommended that you read this *after* the :doc:`quickstart` and understand what Ballad does.

Ballad runs on a core class called :class:`ballad.core.Ballad`. Let's go over a sample program that you might use.

.. code-block:: python

   from ballad import Ballad

   ballad = Ballad()

There are a few things that we can do from here:

* Change the environment from development to production
* Get the data of the lockfile
* Get the identifier of a specific item in the lockfile

.. literalinclude:: ../src/ballad/core.py
   :lines: 21-25

