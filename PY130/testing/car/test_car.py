import unittest
from car import Car

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car()

    def test_car_exists(self):
        self.assertTrue(self.car is not None)

    def test_wheels(self):
        self.assertEqual(4, self.car.wheels)

    def test_name_is_none(self):
        self.assertIsNone(self.car.name)

    def test_instance_car(self):
        self.assertIsInstance(self.car, Car)

    def test_includes_car(self):
        lst = []
        lst.append(self.car)
        self.assertIn(self.car, lst)
    
    def test_raise_initialize_with_arg(self):
        with self.assertRaises(TypeError):
            self.car = Car('Joey')
    
    def test_raise(self):
        with self.assertRaises(ValueError):
            self.car.name = 1234
    
    def test_equality(self):
        self.car.name = 'Toyota'
        other = Car()
        other.name = 'Toyota'

        self.assertEqual(self.car, other)

if __name__ == '__main__':
    unittest.main(verbosity=1)
