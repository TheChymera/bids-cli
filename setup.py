from setuptools import setup, find_packages

packages = find_packages()

setup(
	name="BIDS CLI",
	version="9999",
	description = "BIDS validation for the command line",
	author = "Horea Christian",
	author_email = "chr@chymera.eu",
	url = "https://github.com/TheChymera/bidscli",
	keywords = [
		"bash",
		"command line"
		"data formats",
		"fMRI",
		"minimal",
		"neuroscience",
		"standardization",
		],
	classifiers = [],
	install_requires = [],
	provides = ["bids_cli"],
	packages = packages,
	extras_require = {
		},
	entry_points = {'console_scripts' : \
			['bids = bids_cli.cli:main']
		},
	)
