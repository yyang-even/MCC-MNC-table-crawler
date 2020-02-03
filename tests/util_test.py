#!/usr/bin/env python3

import os
import sys
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


if __name__ == "__main__":
    unittest.main()
