# -*- coding: utf-8 -*- 
from pygit2 import Repository, GIT_SORT_TOPOLOGICAL
from jinja2 import Environment, PackageLoader

import json, sys

def main():
    # repos = {
    #     'name' : pygit2.repository.Repository
    # }
    repos = {}
    # branches = {
    #     'name' : [ pygit2... ]
    # }
    branches = {}
    # commits = {
    #     
    # }
    
    # start by reading the config.json in the current directory
    with open(configFilename, 'r') as conf:
        config = json.load(conf)

    # check if there are no repos defined
    for r in config['repos']:
        repos.update(
            {r['name'] : Repository(r['path'])}
        )    

    if config['output'] == 'json':
        pass

    if config['output'] == 'html':
        # Warning: this shit is not functional! :(
        # :TODO: find a way to setup jinja2 without the use of a module.
        env = Environment(loader=PackageLoader("git2web", "html"))
        template = env.get_template('prototype.html')
        
    return 0

if __name__ == '__main__':
    sys.exit(main())
