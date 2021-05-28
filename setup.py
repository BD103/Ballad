import setuptools

with open("README.md", "rt") as fp:
  long_description = fp.read()


setuptools.setup(
  name="ballad",
  version="1.0.0",
  author="BD103",
  author_email="dont@stalk.me",
  description="For when Poetry just doesn't work.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/BD103/Ballad",
  project_urls={
    "Repository": "https://github.com/BD103/Ballad",
    "Bug Tracker": "https://github.com/BD103/Ballad/issues",
  },
  install_requires=["tomlkit==0.5.11", "click>=8.0.1"],
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
  ],
  package_dir={"": "src"},
  packages=setuptools.find_packages(where="src"),
  python_requires=">=3.8",
)
