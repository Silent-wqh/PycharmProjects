from _11_3_employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    """
    测试雇员
    """
    def setUp(self):
        self.employee_1 = Employee('Steve', 'Jobs', 50000)

    def test_give_default_raise(self):
        self.employee_1.give_raise()
        self.assertEqual(5000, self.employee_1.annual_salary - 50000)

    def test_give_custom_raise(self):
        self.employee_1.give_raise(10000)
        self.assertEqual(10000, self.employee_1.annual_salary - 50000)


if __name__ =='__main__':
    unittest.main()