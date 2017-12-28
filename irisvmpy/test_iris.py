import unittest
from .iris import main

class TestCLIFunction(unittest.TestCase):

	def test_main_output_is_ok(self):
		expected = 'Something'
		got = main()
		self.assertEqual(expected, got)