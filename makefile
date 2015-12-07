## These variables are used for venv
VENV = venv

## These variables are used for webprepare
## The following URLS will suffer from linkrot :(
BOOTSTRAPVERSION = bootstrap-3.3.6-dist
BOOTSTRAPFILE = $(BOOTSTRAPVERSION).zip
BOOTSTRAPURL = https://github.com/twbs/bootstrap/releases/download/v3.3.6/$(BOOTSTRAPFILE)

ANGULARJS = angular.js
ANGULARJSURL = https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular.js

## webprepare follows these steps
## 1. Download and extract bootstrap, moving bootstrap.min.css into html/css/
## 2. Download and move react.js into html/js
## 3. Clean up by removing the zip-file along with the directory
webprepare:
	curl -OL $(BOOTSTRAPURL)
	unzip $(BOOTSTRAPFILE) $(BOOTSTRAPVERSION)/css/bootstrap.css
	if [ ! -d html ]; then mkdir html; fi
	if [ ! -d html/css ]; then mkdir html/css; fi
	if [ ! -d html/js ]; then mkdir html/js; fi
	mv $(BOOTSTRAPVERSION)/css/bootstrap.css html/css/
	curl -OL $(ANGULARJSURL)
	mv $(ANGULARJS) html/js
	rm $(BOOTSTRAPFILE)
	rm -r $(BOOTSTRAPVERSION)

## vnenv follows these steps
## 1. create a virtual enviroment
## 2. install the requirements
venvprepare:
	virtualenv -p /usr/bin/python3 $(VENV)
	$(VENV)/bin/pip install cffi # We need to explicitly install cffi first, since pygit2 depends on it
	$(VENV)/bin/pip install -r requirements.txt

## Remove the downloaded webstuff
webclean:
	rm -rf html/css/*
	rm -rf html/js/$(ANGULARJS)

## Nuke the venv
venvclean:
	rm -rf $(VENV)
