# test_marketdistributor.py
"""
Tests for MarketDistributor module.
"""

import unittest
from marketdistributor import MarketDistributor

class TestMarketDistributor(unittest.TestCase):
    """Test cases for MarketDistributor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MarketDistributor()
        self.assertIsInstance(instance, MarketDistributor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MarketDistributor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
