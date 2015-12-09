# -*- coding: utf-8 -*-
import sys, json, os

from shutil import copyfile
from os.path import join, exists
from jinja2 import Environment, FileSystemLoader
from pygit2 import Repository

class git2web:
    # shitty classname i know, sue me
    def __init__(self, repos):
        # set some initial values
        self.markup = {}

        for name, repo in repos.items():
            self.parse(name, repo)

    def parse(self, name, repo):
        # do not parse empty repos
        if repo.is_empty:
            return

        # set the repo-name as a key to an empty dictionary.
        self.markup.update({name : {'name' : name}})
        self.markup[name].update({'branches' : repo.listall_branches()})

        # iterate over each branch
        for branch in repo.listall_branches():

            br = repo.lookup_branch(branch)
            referenceLog = [reference for reference in br.log()]

            self.markup[name].update(
                {
                    branch : {
                        'name' : branch,
                        'latestDate': repo.revparse_single(br.target.hex).commit_time,
                        'latestHash': br.target.hex,
                        'commits' : {}
                    }
                }
            )

            
            # Watch out for bug-hell right about now
            # good luck debugging this spaghetti code.
            # I listened to this song while coding this shit:
            # https://www.youtube.com/watch?v=SW-BU6keEUw
            for reference in referenceLog:
                oid = str(reference.oid_new)
                commit = repo.revparse_single(oid)
                parents = [str(parent.oid) for parent in commit.parents]
                self.markup[name][branch]['commits'].update(
                    { oid : {
                        'hash'    : oid,
                        'affected': [],
                        'time'    : commit.commit_time, # unix time-format?
                        'parents' : parents,
                        'author'  : commit.committer.name,
                        'message' : commit.message
                    }
                    }
                )

                for twig in commit.tree:
                    self.markup[name][branch]['commits'][oid]['affected'].append({
                        'hash' : twig.hex,
                        'filename' : twig.name
                        # :STRETCH: Individual patches per file, Version 1.1?
                        #  Make it so that a file can have an individual
                        #  patch assigned with it. This was not included
                        #  as a defined goal within the scope of our project;
                })
                    
def main():
    repos = {}
    config = {}
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
        
    if config['markup'] == 'json':
        # :HMM: the json spat out by this if-block gave some warnings
        # on firefox when loading it as text/javascript. Is this present
        # on other JSON files aswell??
        markup = git2web(repos)
        output = json.dumps(markup.markup, sort_keys=True, indent=4)
        path = join(config['outputPath'], "data.json")
        # copy the jsonTemplate to the output-directory.
        jsonTemplate = join(config['templatesDirectory'], config['jsonTemplate'])
        jsonTemplateOutput = join(config['outputPath'], "index.html")
        copyfile(jsonTemplate, jsonTemplateOutput)
        print("[i] Copied {} into {}".format(config['jsonTemplate'], config['outputPath']))

    if not exists(config['outputPath']):
        os.mkdir(config['outputPath'])
    with open(path, 'w') as fh:
        fh.write(output)
    print("[i] wrote markup into", path)

    # copy all the things defined in config['assets']
    # into config['outputPath']
    for asset in config['assets']:
        src = join(config['templatesDirectory'], asset)
        dstFile = join(config['outputPath'], asset)
        dstPath = dstFile[:dstFile.rfind("/")]
        
        if not exists(src):
            print("[!] Unable to find", src) 
            return 1
        if not exists(dstPath):
            os.mkdir(dstPath)
        
        copyfile(src, dstFile)
        
    # smooth sailing, everything is fine!
    return 0

# launch the program at start
if __name__ == '__main__':
    sys.exit(main())
