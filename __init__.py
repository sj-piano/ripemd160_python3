# Imports
import logging




# Relative imports
from . import ripemd160




# ### Notes
# Importing a package essentially imports the package's __init__.py file as a module.




# Collect up the things that we want in the immediate namespace of this module when it is imported.
# This file allows a parent package to run this:
# import ripemd160
# ripemd160.hello()
# result = ripemd160.hash(ascii_input_string)
hello = ripemd160.code.hello.hello
validate = ripemd160.util.validate
configure_module_logger = ripemd160.util.module_logger.configure_module_logger
#submodules = ripemd160.submodules
hash = ripemd160.code.ripemd160.hash




# Set up logger for this module. By default, it produces no output.
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.setLevel(logging.ERROR)
log = logger.info
deb = logger.debug




def setup(
    log_level = 'error',
    debug = False,
    log_timestamp = False,
    log_file = None,
    ):
  # Configure logger for this module.
  ripemd160.util.module_logger.configure_module_logger(
    logger = logger,
    logger_name = __name__,
    log_level = log_level,
    debug = debug,
    log_timestamp = log_timestamp,
    log_file = log_file,
  )
  deb('Setup complete.')
  # Configure modules further down in this package.
  ripemd160.setup(
    log_level = log_level,
    debug = debug,
    log_timestamp = log_timestamp,
    log_file = log_file,
  )

