var git2web = angular.module('git2web', []);

git2web.controller('repoController', ['$scope', '$http', function($scope, $http) {
    this.hash = "";
    this.commit = null;
    this.metadata = null;
    this.branch = "master";
    this.repository = "";
   
    this.init = function() {
	$http.get('/config.json').then(function(data) {
	    $scope.config = angular.fromJson(data.data);
	}, null)
	$http.get('/data.json').then(function(data) {
	    $scope.data = angular.fromJson(data.data);
	}, null)
    };
	
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

    this.selectedCommit = function(paramter) {
	if (parameter == this.commit) {
	    return true;
	}
	return false
    }

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
}]);

