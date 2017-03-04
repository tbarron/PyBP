'''
== Test Driven Development

Write one or more test functions for each program function. Use a test
runner like http://pytest.org/latest/[+py.test+],
https://nose.readthedocs.org/en/latest/[+nosetests+], or
https://pypi.python.org/pypi/green[+green+] to discover and run tests
regularly.

**Why**: Having a comprehensive set of unit tests allows you to make
  changes to your code with confidence. If anything gets broken your
  test suite will let you know.

**How**: Write your test functions in files with names matching
  +test_*.py+, in classes that inherit from unittest.TestCase, with names
  that begin with +"test_"+.

NOTE: py.test will run tests in any class. nosetests will only look in
classes that have "Test" in the name. (!@!Need to verify this)

=== Example

**dates.py**:
----
import time

def date_arith(base, delta, dunits="sec", fmt="%Y.%m%d %H:%M:%S"):
    """
    Compute a delta from a base date and format the result. e.g.

        result = date_arith(time.time(), -3, "day")


    """
    dsec = {'sec': 1,
            'min': 60,
            'hour': 3600,
            'day': 24 * 3600,
            'week': 7 * 24 * 3600}[dunits] * delta

    t = base + dsec
    rval = time.strftime(fmt, time.localtime(t))
    return rval

...
----

**test_dates.py**:
----
import unittest

class TestDateRoutines(unittest.TestCase):
    def test_date_arith(self):
        self.assertEqual("2014.0101 00:00:00",
                         date_arith(1388552400, 0))
        self.assertEqual("2014.0104 00:00:00",
                         date_arith(1388552400, 3, "day"))
        self.assertEqual("2013.1231 17:00:00",
                         date_arith(1388552400, -7, "hour"))
----

**Running the tests**:
----
$ cd <work-dir>
$ py.test 

    or

$ cd <work-dir>
$ nosetests

    or

$ cd <work-dir>
$ green
----
