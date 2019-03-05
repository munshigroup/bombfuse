import sys
import time
import unittest

from bombfuse import timeout, TimeoutError

def sleep_for(seconds):
    secs = 0
    while secs < seconds:
        time.sleep(1)
        secs += 1
        
def test_func(seconds):
    sleep_for(seconds)
    return "completed"
    
class TimeoutTestCase(unittest.TestCase):
    # non-expiry case
    def runTest(self):
        retval = None
        try:
            # wait for 10 seconds as function waits 5 seconds
            retval = timeout(10, test_func, seconds = 5)
        except TimeoutError as e:
            retval = None
        self.assertIsNotNone(retval, "test_func did not return expected value")
        
class TimeoutExpiredTestCase(unittest.TestCase):
    # expiry case
    def runTest(self):
        retval = None
        try:
            # wait for 5 seconds as function waits 10 seconds
            retval = timeout(5, test_func, seconds = 10)
        except TimeoutError as e:
            retval = None
        self.assertIsNone(retval, "test_func failed to time out")

if __name__ == '__main__':
    unittest.main()