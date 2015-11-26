# git2web

## About:

### Dependencies:

  + libgit2
  + jinja2* 
  + pygit2*

(can be installed into a virtualenv via `make venvprepare`)

### Developing:

  Start by running `make webprepare` & `make venvprepare` to set up your
  enviroment. These commands will fetch the required or agreed upon
  libraries that this project uses at the moment.

### UTF-8 all the way!
  
  **PROBLEM:**
  Developing in python gets confusing sometimes when you stumble upon
  a unicode-error, is it because some spooky character was left in your sourcecode
  or what the fuck actually happened?
xo
  **SOLUTION:** 
  Putting `# -*- coding: utf-8 -*-` in the beginning of your `.py`-file
  will make sure that python itself is not confused over what encoding your
  file actually uses.
  
