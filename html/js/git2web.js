var git2web = angular.module('git2web', []);

// much like github, sometimes we want to limit the hash
// lenght, thus this filter.
git2web.filter('sevenLimit', function() {
    return function(input) {
	input = input || '';
	// we don't want to shrink a string
	// that's shorter than our goal
	if(input.length < 7) {
	    return input
	}
	
	var out = input.slice(0,7);
	return out;
    }
});

// very basic stuff for filtering the unix date
// into something more readable
git2web.filter('unixToDatetime', function() {
    return function(input) {
	input = input || '';
	var out = new Date(input * 1000).toLocaleDateString();
	return out; 
    }
});

git2web.controller('repoController', ['$scope', '$http', function($scope, $http) {
    this.hash = "";
    this.commit = null;
    this.metadata = null;
    this.branch = "master";
    this.repository = "";
    this.showBranches = false;
   
    this.init = function() {
	$http.get('/config.json').then(function(data) {
	    $scope.config = angular.fromJson(data.data);
	}, null)
	$http.get('/data.json').then(function(data) {
	    $scope.data = angular.fromJson(data.data);
	}, null)
    };

    this.toggleShowBranches = function() {
	this.showBranches = !this.showBranches;
    }
	    
    this.selectedCommit = function(paramter) {
	if (this.commit = "") {
	    return false
	}
	if (parameter == this.commit) {
	    return true;
	}
	return false
    }

}]);

