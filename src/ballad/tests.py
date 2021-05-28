import tomlkit
import json


def lock_to_json(lock: str="poetry.lock", output: str="out.json"):
  with open(lock, "rt") as f_lock:
    with open(output, "wt") as f_out:
      json.dump(tomlkit.parse(f_lock.read()), f_out, indent=2)
