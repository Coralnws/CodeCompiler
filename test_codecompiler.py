# test_codecompiler.py
"""
Tests for CodeCompiler module.
"""

import unittest
from codecompiler import CodeCompiler

class TestCodeCompiler(unittest.TestCase):
    """Test cases for CodeCompiler class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CodeCompiler()
        self.assertIsInstance(instance, CodeCompiler)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CodeCompiler()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
