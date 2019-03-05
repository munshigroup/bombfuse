import sys
import time
import unittest

from bombfuse import timeout, TimeoutError

def sleep_for(seconds):
    secs = 0
    while secs < seconds:
        time.sleep(1)
        secs += 1
        
def test_case_func():
    sleep_for(5)
    return "completed"
    
def expired_test_case_func():
    sleep_for(10)
    return "completed"
    
class TimeoutTestCase(unittest.TestCase):
    # non-expiry case
    def runTest(self):
        retval = None
        try:
            # wait for 10 seconds as function waits 5 seconds
            retval = timeout(10, test_case_func)
        except TimeoutError as e:
            retval = None
        self.assertIsNotNone(retval, "function did not return expected value")
        
class TimeoutExpiredTestCase(unittest.TestCase):
    # expiry case
    def runTest(self):
        retval = None
        try:
            # wait for 5 seconds as function waits 10 seconds
            retval = timeout(5, expired_test_case_func)
        except TimeoutError as e:
            retval = None
        self.assertIsNone(retval, "function failed to time out")

if __name__ == '__main__':
    unittest.main()