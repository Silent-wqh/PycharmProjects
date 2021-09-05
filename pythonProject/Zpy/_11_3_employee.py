class Employee:
    """测试用雇员类"""

    def __init__(self, firstname, lastname, annual_salary):
        """
        初始化姓名，年薪
        :param firstname:
        :param lastname:
        :param annual_salary:
        """

        self.firstname = firstname
        self.lastname = lastname
        self.annual_salary = annual_salary

    def give_raise(self, increment=5000):
        """
        增加薪水，默认5000
        :param increment:
        :return:
        """
        self.annual_salary += increment
