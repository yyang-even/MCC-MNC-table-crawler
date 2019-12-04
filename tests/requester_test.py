#!/usr/bin/env python3

import os
import sys
import unittest

# Add the parent directory of the script to sys.path
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import requester


class TestStringMethods(unittest.TestCase):

    def test_NotOK(self):
        URL_404 = 'https://en.wikipedia.org/wiki/No_Such_Page'
        self.assertRaises(requester.NotOK, requester.GetPageContentByURL, URL_404)


if __name__ == "__main__":
    unittest.main()
