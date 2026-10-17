# test_pulsebanner.py
"""
Tests for PulseBanner module.
"""

import unittest
from pulsebanner import PulseBanner

class TestPulseBanner(unittest.TestCase):
    """Test cases for PulseBanner class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PulseBanner()
        self.assertIsInstance(instance, PulseBanner)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PulseBanner()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
