import os
import sys

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------
project = "Ballad"
copyright = "2021, BD103"
author = "BD103"

release = "2.0.0"


# -- General configuration ---------------------------------------------------
extensions = ["sphinx.ext.autodoc", "sphinx.ext.coverage", "sphinx.ext.napoleon"]
templates_path = []
exclude_patterns = []
# pygments_style = "murphy"

autodoc_default_options = {"members": True, "undoc-members": True}


# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_static_path = []
html_baseurl = "https://bd103.thedev.id/Ballad"
html_permalinks_icon = "#"
