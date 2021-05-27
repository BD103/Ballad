import os

import toml

from .installer import install


class PyprojectError(Exception):
  pass


def _get_pyproject() -> dict:
  if not os.path.exists("pyproject.toml"):
    raise FileNotFoundError("pyproject.toml does not exist")
    return None

  with open("pyproject.toml", "rt") as fp:
    return toml.load(fp)


def load():
  pypr = _get_pyproject()

  if (
    not pypr["build-system"]["requires"][0].startswith("poetry")
    or not pypr["build-system"]["build-backend"] == "poetry.masonry.api"
  ):
    raise PyprojectError("[build-system] doesn't follow Poetry specification")

  if pypr["tool"]["poetry"].get("dependencies"):
    for dep in pypr["tool"]["poetry"]["dependencies"]:
      if dep == "python":
        continue

      install(dep)

  if pypr["tool"]["poetry"].get("dev-dependencies"):
    for dep in pypr["tool"]["poetry"]["dev-dependencies"]:
      install(dep)
