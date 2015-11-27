# git2web

## About:

### Dependencies:

  + libgit2
  + jinja2* 
  + pygit2*

(can be installed into a virtualenv via `make venvprepare`)

## Developing:

  Start by running `make webprepare` & `make venvprepare` to set up your
  enviroment. These commands will fetch the required or agreed upon
  libraries that this project uses at the moment.

### Contributing

  Please follow these very basic guidelines when contributing code:

  + Document expected function parameter types & any return-value type.

	Example:

	```python
# ...
# parameter x type: string
# parameter y type: integer
# parameter z type: list
# return-type: str
def foo(x, y, z):
    return "bar"
# ...
	```

  + Use `camelCase`, not `this_type_of_code`, even though python itself
  does not adhear to any one particular style, camelCase is the prefered
  style of this project.

## Gotchas

### UTF-8 all the way!
  
  **PROBLEM:**
  Developing in python gets confusing sometimes when you stumble upon
  a unicode-error, is it because some spooky character was left in your sourcecode
  or what the fuck actually happened?

  **SOLUTION:** 
  Putting `# -*- coding: utf-8 -*-` in the beginning of your `.py`-file
  will make sure that python itself is not confused over what encoding your
  file actually uses.

### Virtualenv what?

  If you don't want to use virtualenv, just run `sudo pip install cffi`, followed
  by `sudo pip install -r requirements.txt` to install all the python-dependencies on
  your system.

  If you do plan on using virtualenv, then make sure to run any and all .py-files
  via the virtual enviroment, like so: `$ venv/bin/python myPythonCode.py`
