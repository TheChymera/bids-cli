# BIDS CLI
[![Build Status](https://travis-ci.org/TheChymera/bids-cli.svg?branch=master)](https://travis-ci.org/TheChymera/bids-cli)

This is a light wrapper providing command line access to the functionalities of the new [bidsschematools](https://github.com/bids-standard/bids-specification/tree/master/tools/schemacode/bidsschematools) package.

## Installation

Depending on your preferred package manager you may choose one of the following methods:

#### Portage (e.g. on Gentoo Linux):
BIDS CLI is available via Portage (the package manager of Gentoo Linux, derivative distributions, and installable on [any other Linux distribution](https://wiki.gentoo.org/wiki/Project:Prefix), or BSD) via the [Science Overlay](https://github.com/gentoo/sci).
Upon enabling the overlay, the package can be emerged:

````
emerge bids-cli
````

Alternatively, the live (i.e. latest) version of the package can be installed along with all of its dependencies without the need to enable to overlay:

```
git clone git@github.com:TheChymera/bids-cli.git
cd bids-cli/.gentoo
./install.sh
```

#### Python Package Manager (Users):
Python's `setuptools` allows you to install Python packages independently of your distribution (or operating system, even).
This approach cannot manage any of our numerous non-Python dependencies (by design) and at the moment will not even manage Python dependencies;
as such, given any other alternative, **we do not recommend this approach**:

````
git clone https://github.com/TheChymera/bids-cli.git
cd bids-cli
python setup.py install --user
````

If you are getting a `Permission denied (publickey)` error upon trying to clone, you can either:

* [Add an SSH key](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) to your GitHub account.
* Pull via the HTTPS link `git clone https://github.com/TheChymera/bids-cli.git`.

#### Python Package Manager (Developers):
Python's `setuptools` allows you to install Python packages independently of your distribution (or operating system, even);
it also allows you to install a "live" version of the package - dynamically linking back to the source code.
This permits you to test code (with real module functionality) as you develop it.
This method is sub-par for dependency management (see above notice), but - as a developer - you should be able to manually ensure that your package manager provides the needed packages.

````
git clone git@github.com:TheChymera/bids-cli.git
cd bids-cli
echo "export PATH=\$HOME/.local/bin/:\$PATH" >> ~/.bashrc
source ~/.bashrc
python setup.py develop --user
````

If you are getting a `Permission denied (publickey)` error upon trying to clone, you can either:

* [Add an SSH key](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) to your GitHub account.
* Pull via the HTTPS link `git clone https://github.com/TheChymera/bids-cli.git`.

## Dependencies

The most precise specification of the dependency graph (including conditionality) can be extracted from the [bids-cli ebuild](.gentoo/sci-biology/bids-cli/bids-cli-99999.ebuild).
For manual dependency management and overview you may use the following list:

* [argh](https://github.com/neithere/argh)
* [bidsschematools](https://github.com/bids-standard/bids-specification/tree/master/tools/schemacode/bidsschematools)

