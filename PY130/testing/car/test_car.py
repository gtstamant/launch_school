import unittest
from car import Car

class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car()
    
    def test_car_exists(self):
        self.assertTrue(self.car is not None)
    
    def test_wheels(self):
        self.assertEqual(4, self.car.wheels)

    def test_name_is_none(self):
        self.assertIsNone(self.car.name)
    
    def test_instance_of_car(self):
        self.assertIsInstance(self.car, Car)
    
    def test_includes_car(self):
        arr = [1, 2, 3]
        arr.append(self.car)
        self.assertIn(self.car, arr)
    
    def test_raise_initialize_with_arg(self):
        with self.assertRaises(TypeError):
            car = Car(name="Joey")

    def test_set_name_raises(self):
        self.assertRaises(ValueError, setattr, self.car, 'name', 1234)
    
    def test_value_equality(self):
        car1 = Car()
        car2 = Car()

        car1.name = 'Kim'
        car2.name = 'Kim'

        self.assertEqual(car1, car2)

if __name__ == '__main__':
    unittest.main()