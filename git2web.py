# -*- coding: utf-8 -*-
import sys, json

from jinja2 import Template
from pygit2 import Repository

class git2html:
    pass

class git2json:
    """
Coming in, the repos variable is defined as follows:
{'repositoryName' : pygit2.repository.Repository-object}
    """
        
    def __init__(self, repos):
        # set some initial values
        self.json = {}
    
        for name, repo in repos:
            self.parse(name, repo)

    def parse(name, repo):
        # do not parse empty repos
        if repo.is_empty():
            return

        # set the repo-name as a key to an empty dictionary.
        self.json.update({name : {}})

        # iterate over each branch
        for branch in repo.listall_branches():
            self.json[name].update(
                { branch : {}}
            )

            br = repo.lookup_branch(branch)
            commits = [commit for commit in br.log()]
            
            # Watch out for bug-hell right about now
            # good luck debugging this spaghetti code.
            # I listened to this song while coding this shit:
            # https://www.youtube.com/watch?v=SW-BU6keEUw
            for commit in commits:
                # reference the commit by oid
                oid = commit.oid_new
                self.json[name][branch].update(
                    { oid : {
                        'affected': [{
                            'filename' : en.name,
                            'insertions' : en.tree.diff_to_tree().stats.insertions,
                            'deletions' : en.tree.diff_to_tree().stats.deletions,
                            'patch': en.tree.diff_to_tree().patch # this could be improved* 
                        } for en in repo.revparse_single(oid)],
                        'parent'  : commit.oid_old,
                        'author'  : commit.commiter,
                        'message' : commit.message
                    }
                    }
                )
                
                self.json[name][branch][oid]

    # * commit.tree.diff_to_tree().patch displays
    # an included command, along with pure diff syntax,
    # which is good in its own way (we can use pygments
    # for syntax highlighting; but the leading command
    # (diff --git ...) would be garbage text.
                
def main():
    repos, config = {}, {}

    # read the config
    with open('config.json', 'r') as conf:
        config = json.load(conf)

    # iterate over all specified repository
    for r in config['repos']:
        try:
            repos.update({r['name'] : Repository(r['path'])}) 
        except KeyError:
            print('Unable to open repository {} in config. Wrong path?'.format(r['name']))
            return 1

    # generate our model-objects here

    if config['markup'] == 'html':
        # do stuff with jinja2 here
        pass

    if config['markup'] == 'json':
        # do stuff with json here
        pass

    # smooth sailing, everything is fine!
    return 0

# launch the program at start
if __name__ == '__main__':
    sys.exit(main())
        

        
        
                         

