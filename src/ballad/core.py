"""core.py
----------

This module contains the base class Ballad.
"""

import os
import subprocess

import tomlkit


class Ballad(object):
  """Contains all the functions necessary for Ballad's core operations.

    Attributes:
      lockfile_name (str): The filename of the lockfile.
      install_quiet_flag (str): If not verbose in `install_identifier`, then what flag to use to make it quiet.
      environment (str): Can be development or production. Decides which dependencies to install."""

  def __init__(self):
    """Initializes object. No arguments necessary."""
    self.lockfile_name = "poetry.lock"
    self.install_quiet_flag = "-q"
    self.environment = "development"

  def lockfile(self) -> tomlkit.items.AoT:
    """Loads a Poetry lockfile and returns an array of tables.

        Returns:
          tomlkit.items.AoT: List of dictionaries
        """
    if os.path.isfile(self.lockfile_name):
      with open(self.lockfile_name, "rt") as fp:
        return tomlkit.parse(fp.read())["package"]
    else:
      raise FileNotFoundError(f"Cannot find {self.lockfile_name}")

  def get_identifier(self, table: dict) -> str:
    """Reads lockfile table and returns an identifier.

        Args:
          table (dict): Read from parsed lockfile

        Returns:
          str: String to be appended to ``pip install`` command
        """

    # If PyPI dep
    if not table.get("source"):
      return f"{table['name']}=={str(table['version'])}"
    elif table["source"]["type"] == "git":
      return f"git+{table['source']['url']}@{table['source']['resolved_reference']}#egg={table['name']}"
    elif table["source"]["type"] == "url":
      return table["source"]["url"]
    elif table["source"]["type"] == "file":
      return table["source"]["url"]
    else:
      return "ballad"

  def install_identifier(self, table: dict, verbose: bool = False):
    """Installs specific dependency from item in lockfile table.

        This is used for a single specific dependecy. Parse a lockfile with Tomlkit, then run this function with a specific item in that list. If you wish to just install the entire lockfile, used ``Ballad.install()`` instead.

        Args:
          table (dict): Item in lockfile table
          verbose (:obj:`bool`, optional): Whether to show PIP installation process.
        """
    if verbose:
      subprocess.run(["python", "-m", "pip", "install", self.get_identifier(table)])
    else:
      subprocess.run(
        [
          "python",
          "-m",
          "pip",
          "install",
          self.install_quiet_flag,
          self.get_identifier(table),
        ]
      )

  def install(self, quiet: bool = False):
    """Loops through lockfile and installs dependencies.

        Recommended method of installing from lockfile.

        Args:
          quiet (:obj:`bool`, optional): If true it will not notify which dependencies it installs.
        """
    for table in self.lockfile():
      if self.environment == "production" and table["category"] == "dev":
        continue

      if not quiet:
        print("Installing", self.get_identifier(table))

      self.install_identifier(table)
