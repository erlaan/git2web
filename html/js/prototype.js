var git2web = angular.module('git2web', []);

git2web.controller('repoCtrl', function($http) {

    this.projectName = "git2web";
    this.hash = "";
    this.commit = null;
    this.metadata = null;
    this.repository = "";
    // :TODO: replace this with something read from JSON
    // :TODO-BEFORE: Fix the python-script to actually output some JSON
    // commits holds all the commits
	

    // this.dickhead = "";oo

      $http.get('../../config.json')
       .success(function(res){
          this.dickhead = res.repos;                
        });

    console.log(this.dickhead);


    this.commits = {
	'66c3d95af0c89833e363780f8255d0da23a6f9b8': {
	    'afectedFiles': [
		{
		    'filename': 'AVeryLongFilenameJustToTestHowItLooksLike.c',
		    'insertions': 234,
		    'deletions': 20,
		    'patch': "hello world!"
		},
		{
		    'filename': 'makefile',
		    'insertions': 134,
		    'deletions': 10,
		    'patch': "hello hoe!"
		},
		{
		    'filename': "bitch.h",
		    'insertions': 222,
		    'deletions': 999,
		    'patch': "hello bro!"
		}
	    ],
	    'author': 'jh <jonatanhaltorp@gmail.com>',
	    'message': 'updated makefile, sketching template',
	},
	'580476ae2def594645cd71ee3d98eccf41e0d2b5': {
	    'affectedFiles': [
		{
		    'filename': 'heyall.c',
		    'insertions': 234,
		    'deletions': 20,
		    'patch': "hello world!"
		},
		{
		    'filename': 'makefile',
		    'insertions': 134,
		    'deletions': 10,
		    'patch': "hello hoe!"
		},
		{
		    'filename': "heyall.h",
		    'insertions': 222,
		    'deletions': 999,
		    'patch': "hello bro!"
		}
	    ],
	    'author': 'Erlaan <firensonic@sandia-gaming.se>',
	    'message': 'Did add charset to the template!',
	},
	'9d0eb9c584153e38c76793128d7a1e00fb9e9ce1': {
	    'affectedFiles': [
		{
		    'filename': 'hoe.c',
		    'insertions': 234,
		    'deletions': 20,
		    'patch': "hello world!"
		},
		{
		    'filename': 'makefile',
		    'insertions': 134,
		    'deletions': 10,
		    'patch': "hello hoe!"
		},
		{
		    'filename': "hoe.h",
		    'insertions': 222,
		    'deletions': 999,
		    'patch': "hello bro!"
		}
	    ],
	    'author': 'Erlaan <firensonic@sandia-gaming.se>',
	    'message' : 'The begining of the template.html'
	}
    };

    this.selected = function(parameter) {
	if (parameter != "") {
	    return true;
	}
	return false;
    }
    
    this.setCommitMetadata = function(metadata) {
	this.commitMetadata = metadata;
    };

    this.displayNewCommit = function(hash) {
	this.commit = this.commits[hash];
	this.hash = hash;
	this.setCommitMetadata(this.commit.affectedFiles);
    };
});

