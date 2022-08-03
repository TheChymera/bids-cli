from bidsschematools.validator import validate_bids

import inspect


# Setting up wrappers to prevent returns
def validate(*args):
	_ = validate_bids(*args)

# Adapting wrapper docstrings and signatures:
validate.__signature__ = inspect.signature(validate_bids)
validate.__doc__ = validate_bids.__doc__
