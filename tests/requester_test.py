#!/usr/bin/env python3

import os
import sys
import unittest
from unittest.mock import patch
from unittest.mock import Mock

# Add the parent directory of the script to sys.path
sys.path.insert(1, os.path.join(sys.path[0], ".."))

import requester


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.EXPECTED_CONTENT = "Page Content"
        self.ENCODING = "utf-8"
        self.URL = "Mock URL"

    def createMockResponse(self, status_code):
        headers_dictionary = {"content-type": "HTML"}
        mock_response = Mock(
            status_code=status_code,
            headers=headers_dictionary,
            encoding=self.ENCODING,
            text=self.EXPECTED_CONTENT,
        )

        return mock_response

    @patch("requester.requests", autospec=True)
    def test_OK(self, mock_requests):
        mock_requests.get.return_value = self.createMockResponse(200)
        self.assertEqual(
            self.EXPECTED_CONTENT, requester.GetPageContentWithLogging(self.URL)
        )


if __name__ == "__main__":
    unittest.main()
