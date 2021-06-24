Quickstart
==========

Ballad has many reasonable defaults, so you usually won't find a need to configure anything.

Ballad is meant to be run in the command line, but it also supports a Python API.

.. code-block:: console

   $ python -m ballad --help
   Usage: python -m ballad [OPTIONS] COMMAND [ARGS]...

     Install Poetry Project without Poetry

   Options:
     --help  Show this message and exit.

   Commands:
     convert-lock  Reads lockfile, convert it to JSON, then outputs...
     install       Install dependencies from lockfile using PIP

The CLI exposes the most useful command of Ballad, ``install``.

.. code-block:: console

   $ python -m ballad install --help
   Usage: python -m ballad install [OPTIONS]

     Install dependencies from lockfile using PIP

   Options:
     -d, --development / -p, --production
     -l, --lockfile TEXT
     -q, --quiet
     --help                          Show this message and exit.

The install command has many sensible defaults. For one, it assumes that you want to install your development dependencies. It also assumes that your lockfile name is ``poetry.lock``. All you need to do is run:

.. code-block:: console

   $ python -m ballad install
