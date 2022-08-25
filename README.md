# Description

A pure Python 3 implementation of the RIPEMD-160 hash algorithm.




# Sample commands


```bash

python3 cli.py

python3 cli.py --help

python3 cli.py --task hello

python3 cli.py --task hello --log-level=info

python3 cli.py --task hello --log-level=debug

python3 cli.py --task get_python_version

python3 cli.py --task get_ripemd160 --data "hello world"

python3 cli.py --task get_ripemd160 --file ripemd160/data/data1.txt

```


Tests:

```bash

# Run all tests, including submodule tests.
pytest3

# Run all tests in a specific test file
pytest3 ripemd160/test/test_hello.py

# Run tests with relatively little output
pytest3 --quiet ripemd160/test/test_hello.py

# Run a single test
pytest3 ripemd160/test/test_hello.py::test_hello

# Print log output in real-time during a single test
pytest3 --capture=no --log-cli-level=INFO ripemd160/test/test_hello.py::test_hello

# Note: The --capture=no option will also cause print statements within the test code to produce output.

```



Code style:


```bash

pycodestyle ripemd160/code/hello.py

pycodestyle --filename=*.py

pycodestyle --filename=*.py --statistics

pycodestyle --filename=*.py --exclude ripemd160/submodules

```

Settings for pycodestyle are stored in the file `tox.ini`.




# Environment

Successfully run under the following environments:

1:  
- Ubuntu 16.04 on WSL (Windows Subsystem for Linux) on Windows 10  
- Python 3.5.2  
- pytest 6.1.2  






# Background

Original code:  
http://www.bjrn.se/code/ripemdpy.txt

> pure Python implementation of the RIPEMD-160 algorithm.

Author: Bjorn Edstrom

Ported with some restructuring to Python 3 by Nicholas Piano.

Re-formatted into its current package layout by StJohn Piano.

