var git2web = angular.module('git2web', []);

git2web.controller('repoCtrl', function($scope, $http) {

    this.projectName = "git2web";
    this.hash = "";
    this.commit = null;
    this.metadata = null;
    this.branch = "";
    this.repository = "";

    $http.get('/config.json').success(function(res) {
	setTimeout(function() {
	    $scope.config = res;
	}, 500);
    });
	

    $http.get('/data.json').success(function(res) {
	setTimeout(function(){
	    $scope.jsondata = res;
	}, 500);
    });

    // helperfunction for checking if a branch is selected
    this.selectedBranch = function(parameter) {
	if (parameter == this.branch) {
	    return true;
	}
	return false;
    };
    
    this.selectedRepo = function(parameter) {
	if (parameter == this.repository) {
	    return true;
	}
	return false;
    };

    this.displayNewRepo = function(repo) {
	this.repository = repo;
	// default to show the master-branch of a repository.
	this.selectedBranch = "master";
    };

    this.displayNewCommit = function(hash) {
	this.commit = this.commits[hash];
	this.hash = hash;
	this.commitMetadata = this.commit.affectedFiles;
    };

    this.log = function(obj) {
	console.log(obj);
    };
    
});

