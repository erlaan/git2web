# -*- coding: utf-8 -*-
import sys, json, os

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

        for name, repo in repos.items():
            self.parse(name, repo)

    def parse(self, name, repo):
        # do not parse empty repos
        if repo.is_empty:
            return

        # set the repo-name as a key to an empty dictionary.
        self.json.update({name : {}})

        # iterate over each branch
        for branch in repo.listall_branches():
            self.json[name].update(
                { branch : {}}
            )

            br = repo.lookup_branch(branch)
            referenceLog = [reference for reference in br.log()]
            
            # Watch out for bug-hell right about now
            # good luck debugging this spaghetti code.
            # I listened to this song while coding this shit:
            # https://www.youtube.com/watch?v=SW-BU6keEUw
            for reference in referenceLog:
                oid = str(reference.oid_new)
                commit = repo.revparse_single(oid)
                parents = [str(parent.oid) for parent in commit.parents]
                self.json[name][branch].update(
                    { oid : {
                        'affected': [],
                        'time'    : commit.commit_time, # unix time-format?
                        'parents' : parents,
                        'author'  : commit.committer.name,
                        'message' : commit.message
                    }
                    }
                )

                for twig in commit.tree:
                    self.json[name][branch][oid]['affected'].append({
                        'hex' : twig.hex,
                        'filename' : twig.name
                        # :STRETCH: Individual patches per file, Version 1.1?
                        #  Make it so that a file can have an individual
                        #  patch assigned with it. This was not included
                        #  as a defined goal within the scope of our project;
                })

    # * commit.tree.diff_to_tree().patch displays
    # an included command, along with pure diff syntax,
    # which is good in its own way (we can use pygments
    # for syntax highlighting; but the leading command
    # (diff --git ...) would be garbage text.
    # 
    # ** raises an TypeError exception, '_pygit2.commit' object is not iterable.
    # What i want the code to do:
    #  iterate over every changed file in the commit & create some structures based
    # on that data; IS THAT SO FRICKIN HARD?!?!? /(; c_ ; /)
    # :TODO: find the right object to iterate over.
    #
    # *** WOULD contain these pieces of information, but who the fuck coded this
    # piece of shit library??! Why is there so much complexity?!! I can fetch the
    # binary diff of a moth's fart from nineteen years ago but not get number
    # of inserted/deleted lines? W T F
    # I do not claim to know any and all insides of pygit2 or git.
    # So my thoughts come from lack of understanding, because there should
    # be a way to do it.
    

                
def main():
    repos, config = {}, {}
    markup = ""

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
        parser = git2json(repos)
        markup = json.dumps(parser.json)
        path   = os.path.join(config['outputPath'], 'data.json')
        if not os.path.exists(config['outputPath']):
            os.mkdir(config['outputPath'])
        with open(path, 'w') as fh:
            fh.write(markup)
        print("[i] wrote markup into", path)
        
    # :TODO: copy generated markup, along with any template-files to
    # the config['output']

    # smooth sailing, everything is fine!
    return 0

# launch the program at start
if __name__ == '__main__':
    sys.exit(main())
        

        
        
                         

