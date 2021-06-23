Patch Notes
===========

`2.0.0 <https://pypi.org/project/ballad/2.0.0/>`_
-----------------------------------------------------

Major update supporting a new API and core.

* Complete rewrite, so 1.1.0 programs do not work
* Sphinx Documentation (What you're reading right now!)
* Object-Oriented Core instead of functions
* Renaming of ``test.py`` to ``utils.py``
* Tomlkit dependency updated
* Support of special dependencies, including

  * Git
  * URL
  * File

* Rework of CLI

`2.0.0a2 <https://pypi.org/project/ballad/2.0.0a2/>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Direct update to 2.0.0a1 with a basic CLI. This project was initially used in the `ReplAPI-it Projects <https://github.com/ReplAPI-it/ReplAPI.it-Python>`_ for Github actions. When BD103 realized that there was no way to reach Ballad through the CLI in 2.0.0a1, he quickly updated to 2.0.0a2.

`2.0.0a1 <https://pypi.org/project/ballad/2.0.0a1/>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pre-release with new API.

`1.1.0 <https://pypi.org/project/ballad/1.1.0/>`_
-------------------------------------------------

Now supports converting lockfiles to JSON with ``ballad.tests.convert_lock``.

`1.0.0 <https://pypi.org/project/ballad/1.0.0/>`_
-------------------------------------------------

Initial release, supports PyPI dependencies.