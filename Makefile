clean:

	# remove cache files
	rm -rf **/__pycache__ **/.pytest_cache

	# remove example output
	rm -rf examples/*.pdf examples/*.tex

refresh-git-index:

	# remove all items from git index
	git rm -r --cached .
