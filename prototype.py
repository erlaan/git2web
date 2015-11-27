# -*- coding: utf-8 -*-
import sys
from pygit2 import Repository

def main():
    # Read in a repository
    repo = Repository("./")

    # list the changed files in the most recent commit (HEAD)
    commit = repo.revparse_single("HEAD")

    # iterate and print every blob in the commit
    for entry in commit.tree:
        print(entry.id, entry.type, entry.name)
    
    # Everything went as planned
    return 0

if __name__ == '__main__':
    sys.exit(main())






