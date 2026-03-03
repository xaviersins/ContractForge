# test_contractforge.py
"""
Tests for ContractForge module.
"""

import unittest
from contractforge import ContractForge

class TestContractForge(unittest.TestCase):
    """Test cases for ContractForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ContractForge()
        self.assertIsInstance(instance, ContractForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ContractForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
