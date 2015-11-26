# The following URLS will suffer from linkrot :(
BOOTSTRAPVERSION = bootstrap-3.3.6-dist
BOOTSTRAPFILE = $(BOOTSTRAPVERSION).zip
BOOTSTRAPURL = https://github.com/twbs/bootstrap/releases/download/v3.3.6/$(BOOTSTRAPFILE)

REACTJS = react-0.14.3.min.js
REACTJSURL = https://fb.me/react-0.14.3.min.js

setup:
	curl -OL $(BOOTSTRAPURL)
	unzip $(BOOTSTRAPFILE) $(BOOTSTRAPVERSION)/css/bootstrap.min.css
	mv $(BOOTSTRAPVERSION)/css/bootstrap.min.css html/css/
	curl -OL $(REACTJSURL)
	mv $(REACTJS) html/js
	rm $(BOOTSTRAPFILE)
	rm -r $(BOOTSTRAPVERSION)
