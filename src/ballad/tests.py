import json
import os

import tomlkit


def convert_lock(lock: str = "poetry.lock", output: str = "poetry.json"):
  if not os.path.isfile(lock):
    raise FileNotFoundError(f"Cannot find {lock}")

  with open(lock, "rt") as f_lock:
    with open(output, "wt") as f_out:
      json.dump(tomlkit.parse(f_lock.read()), f_out, indent=2)
