"""utils.py
-----------

This module includes various utilities that are handy for the development process and debugging. Feel free to poke around!
"""


import json
import os

import tomlkit


def convert_lock(lock: str = "poetry.lock", output: str = "poetry.json"):
  """Loads lockfile converts it to JSON.

    Args:
      lock (str): Filename of lockfile
      output (str): Filename to write JSON to

    Raises:
      FileNotFoundError: Cannot find the lockfile
    """
  if not os.path.isfile(lock):
    raise FileNotFoundError(f"Cannot find {lock}")

  with open(lock, "rt") as f_lock:
    with open(output, "wt") as f_out:
      json.dump(tomlkit.parse(f_lock.read()), f_out, indent=2)
