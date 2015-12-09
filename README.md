# git2web

## About:

**Git2Web** reads in information about a git-project and spits out
JSON-formatted data for you to use however you like. We provide a
basic, default Angular app that creates a website around the data.

You can change various settings in config.json, like where your
templates are located, where your assets are located and so on.
Git2web will copy these files into the specified output folder
(_markup) by default.

Git2Web is in *early* stages of development, pull-requests & issues or
general constructive feedback is welcomed with open arms.

Because Git2Web is configured through config.json, you don't need to
remember passing it any flag, you just run it.

```
$ # Preparing the environment
$ make webprepare
...

$ # Preparing the virtualenv
$ make venvprepare
...

$ # Running git2web
$ venv/bin/python3 git2web.py
```

### Sytem Dependencies:
  + libffi
  + libgit2

### Python Dependencies:
  + pygit2

### Preparing:

  Start by running `make webprepare` & `make venvprepare` to set up your
  enviroment. These commands will fetch the required or agreed upon
  libraries that this project uses at the moment.

  Running `make webclean` & `make venvclean` will simply remove the files
  created by their 'prepare'-counterpart.

### Virtualenv what?

  If you don't want to use virtualenv, just run `sudo pip install cffi`, followed
  by `sudo pip install -r requirements.txt` to install all the python-dependencies on
  your system.

  If you do plan on using virtualenv, then make sure to run any and all .py-files
  via the virtual enviroment, like so: `$ venv/bin/python myPythonCode.py`
