#!/usr/bin/env python3

import os
import sys
import time
import unittest

# Add the parent directory of the script to sys.path
sys.path.insert(1, os.path.join(sys.path[0], ".."))

import util


class TestRemoveParenthesesAndWithin(unittest.TestCase):
    def test_Sanity(self):
        self.assertEqual("Bands", util.RemoveParenthesesAndWithin("Bands (MHz)"))

    def test_MakeNoChangesIfNoParentheses(self):
        a_string = "Bands "
        self.assertEqual(a_string, util.RemoveParenthesesAndWithin(a_string))


SLEEP_INTERVAL_SECONDS = 1


@util.PacedCall(SLEEP_INTERVAL_SECONDS)
def VoidFunc():
    pass


@util.PacedCall(SLEEP_INTERVAL_SECONDS)
def AnotherVoidFunc():
    pass


class TestPacedCall(unittest.TestCase):
    def test_FirstCallShouldTakeNoTime(self):
        start_time = time.perf_counter()
        VoidFunc()
        end_time = time.perf_counter()
        run_time = end_time - start_time
        self.assertLess(run_time, SLEEP_INTERVAL_SECONDS)

    def test_CallTwiceShouldTakeOneInterval(self):
        start_time = time.perf_counter()
        AnotherVoidFunc()
        AnotherVoidFunc()
        end_time = time.perf_counter()
        run_time = end_time - start_time
        self.assertGreater(run_time, SLEEP_INTERVAL_SECONDS)
        self.assertLess(run_time, SLEEP_INTERVAL_SECONDS * 2)


if __name__ == "__main__":
    unittest.main()
