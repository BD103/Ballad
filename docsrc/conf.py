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
pygments_style = "manni"

autodoc_default_options = {"members": True, "undoc-members": True}


# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
html_static_path = []
html_baseurl = "https://bd103.thedev.id/Ballad"
html_permalinks_icon = "#"

_html_theme_colors = {
  "anchor": "#00AA88",
  "anchor_hover_bg": "transparent",
  "anchor_hover_fg": "#336666",
  "link": "#006699",
  "link_hover": "#0099FF",
  "font_family": "\"Helvetica\", \"Arial\", sans-serif",
  "head_font_family": "\"Georgia\", serif"
}

html_theme_options = {
  "github_user": "BD103",
  "github_repo": "Ballad",
  "description": "For when Poetry just doesn't work.",
  **_html_theme_colors
}