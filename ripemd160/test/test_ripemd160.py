# Imports
import pytest
import pkgutil




# Relative imports
from .. import code
from .. import util
from .. import submodules




# Shortcuts
from ..code import ripemd160




# Setup for this file.
@pytest.fixture(autouse=True, scope='module')
def setup_module(pytestconfig):
  # If log_level is supplied to pytest in the commandline args, then use it to set up the logging in the application code.
  log_level = pytestconfig.getoption('log_cli_level')
  if log_level is not None:
    log_level = log_level.lower()
    code.setup(log_level = log_level)
    submodules.setup(log_level = log_level)




# ### SECTION
# Basic checks.


def test_hello():
  x = ripemd160.hash('hello world')
  assert x == '98c615784ccb5fe5936fbc0cbe9dfdb408d92f0f'


def test_hello_data():
  data_file = '../data/data1.txt'
  data = pkgutil.get_data(__name__, data_file).decode('ascii').strip()
  assert data == 'hello world'
  x = ripemd160.hash(data)
  assert x == '98c615784ccb5fe5936fbc0cbe9dfdb408d92f0f'


def test_empty_string():
  x = ripemd160.hash('')
  assert x == '9c1185a5c5e9fc54612808977ee8f548b2258d31'


def test_a():
  x = ripemd160.hash('a')
  assert x == '0bdc9d2d256b3ee9daae347be6f4dc835a467ffe'


def test_abc():
  x = ripemd160.hash('abc')
  assert x == '8eb208f7e05d987a9b044a8e98c6b087f15a0bfc'


def test_alphabet():
  x = ripemd160.hash('abcdefghijklmnopqrstuvwxyz')
  assert x == 'f71c27109c692c1b56bbdceb5b9d2865b3708dbc'


def test_alphanumeric():
  x = ripemd160.hash('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
  assert x == 'b0e20b6e3116640286ed3a87a5713079b21f5189'


def test_lorem_ipsum():
  x = ripemd160.hash('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
  assert x == '24d4e5dbf4d51fbcb545dc334be670c55d702d60'


def test_64_bytes():
  x = ripemd160.hash("A string with a length of exactly 64 bytes. [filler text .....]")
  assert x == 'c20be0527e6280c0c9218dca292843bbbed537bf'


def test_fox_1():
  x = ripemd160.hash('The quick brown fox jumps over the lazy dog')
  assert x == '37f332f68db77bd9d7edd4969571ad671cf9dd3b'


def test_fox_1():
  x = ripemd160.hash('The quick brown fox jumps over the lazy cog')
  assert x == '132072df690933835eb8b6ad0b77e7b6f14acad7'



