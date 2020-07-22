clean:

	# remove all cache files
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf

	# remove example output
	rm -rf examples/*.pdf examples/*.tex

	# remove base-level auxillary/log files
	rm -rf *.out *.aux *.log

flake:

	# run flake8 style guide checking
	flake8 --config setup.cfg

refresh-git-index:

	# remove all items from git index
	git rm -r --cached .
