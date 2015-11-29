var git2web = angular.module('git2web', []);

git2web.controller('metadata', function() {
    // meta holds metadata on the repository.
    this.meta = {'name': 'Git2Web'}; // :TODO: replace this with something read from JSON    
});

git2web.controller('repoCtrl', function() {
    // commits holds all the commits
    //var commits = []; // :TODO: replace this with something read from JSON
    this.commits = [
	{
	    'commit':'66c3d95af0c89833e363780f8255d0da23a6f9b8',
	    'author': 'jh <jonatanhaltorp@gmail.com>',
	    'date': 'Sun Nov 29 12:58:02 2015 +0100',
	    'message': 'updated makefile, sketching template'
	},
	{
	    'commit': '580476ae2def594645cd71ee3d98eccf41e0d2b5',
	    'author': 'Erlaan <firensonic@sandia-gaming.se>',
	    'date': 'Sun Nov 29 10:40:20 2015 +0100',
	    'message': 'Did add charset to the template!'
	},
	{
	    'commit': '9d0eb9c584153e38c76793128d7a1e00fb9e9ce1',
	    'author': 'Erlaan <firensonic@sandia-gaming.se>',
	    'date': 'Sun Nov 29 09:30:07 2015 +0100',
	    'message' : 'The begining of the template.html'
	}
    ];    

    this.show = function(commit) {
	console.log(commit)
    }; 
});





