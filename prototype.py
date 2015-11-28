# -*- coding: utf-8 -*-
import git2web
from jinja2 import Environment, PackageLoader
import sys
from pygit2 import Repository

env = Environment(loader=PackageLoader("git2web", "html"))
template = env.get_template('prototype.html')
# just print the damn thing for now.

repo = Repository("./")
branch = repo.lookup_branch('master')
print(template.render(tree=branch.log()))

exit(0)
