import unittest
from test_material import (TestClass, 
                           NoExperienceError, 
                           Employee, 
                           Number, 
                           Numeric,
                           Lst)

class TestTestClass(unittest.TestCase):
    def test_odd(self):
        value = 11
        self.assertTrue(value % 2 != 0, 'value is not odd')
    
    def test_lower(self):
        value = 'XYz'
        self.assertEqual('xyz', value.lower())
    
    def test_none(self):
        value = None
        self.assertIsNone(value)

    def test_presence(self):
        value = 'xyz'
        collection = (1, 2, 'xyz')
        self.assertIn(value, collection)
    
    def test_absence(self):
        value = 'xyz'
        collection = (1, 2, 3)
        self.assertNotIn(value, collection)
    
    def test_error(self):
        with self.assertRaises(NoExperienceError):
            employee = Employee()
            employee.hire()
    
    def test_error_short_(self):
        employee = Employee()
        self.assertRaises(NoExperienceError, Employee.hire, employee)
    
    def test_class(self):
        obj = Numeric()
        self.assertIsInstance(obj, Numeric)
    
    def test_process(self):
        lst = Lst()
        self.assertIs(lst, lst.process())

if __name__ == "__main__":
    unittest.main()