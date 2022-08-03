__author__ = "Horea Christian"

import argh

from .wrappers import validate


def main():
	argh.dispatch_commands([validate,])

if __name__ == '__main__':
	main()
