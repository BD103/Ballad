import os
import subprocess

import tomlkit


def _check_lock() -> bool:
  if not os.path.isfile("poetry.lock"):
    raise FileNotFoundError("Cannot find poetry.lock")
    return False
  else:
    return True


def _get_lock() -> dict:
  if _check_lock():
    with open("poetry.lock", "rt") as fp:
      return tomlkit.parse(fp.read())["package"]
  else:
    return {}


def _install(i: dict, quiet: str = "-qq", debug: bool = False):
  if debug:
    print("Installing", i["name"], "==", i["version"])

  subprocess.run(
    ["python", "-m", "pip", "install", quiet, i["name"] + "==" + str(i["version"])]
  )


def load_all(quiet: str = "-qq", debug: bool = False):
  for i in _get_lock():
    _install(i, quiet, debug)


def load_production(quiet: str = "-qq", debug: bool = False):
  for i in _get_lock():
    if i["category"] == "main":
      _install(i, quiet, debug)
