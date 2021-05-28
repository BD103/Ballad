# [Ballad](https://github.com/BD103/Ballad)

> For when Poetry just doesn't work.

Have you tried setting up [Poetry](https://python-poetry.org/), but something doesn't work? Maybe you're...

- Trying to implement Github Actions but the commands don't register.
- Testing on a computer that doesn't have Poetry installed.
- Just wanting to test out a package without any of these crazy dependency managers.

If so, then you're in the right place!

## Install and Use

First install:

```console
$ pip install ballad
```

Want to install dependencies? Run:

```console
$ python -m ballad install
```

There are various options that you can also run. Check them out!

## Contributing

Get the source code with:

```console
$ git clone https://github.com/BD103/Ballad.git
$ cd Ballad
$ pip install -r requirements.txt
```

Check over your code with the following commands:

```console
$ black .
$ isort .
$ flake8
```

Create a PR, thanks for helping!
