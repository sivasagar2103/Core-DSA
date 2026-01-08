'''
'''

#Before
class Employee:
    def __init__(self, name, email, salary):
        self._name = name
        self._email = email
        self._salary = salary
    
    def calculate_salary(self):
        pass

    def save_to_database(self):
        pass

    def generate_payslip(self):
        pass

    def send_payslip_mail(self):
        pass


#After
class Employee:
    def __init__(self, name, email, age):
        self._name = name
        self._email = email
        self._age = age
    
    def get_name(self):
        return self._name
    
    def get_email(self):
        return self._email


class Salary:
    def __init__(self, amt):
        self._amt = None
    

    def calculate_net(self):
        pass


class Payslip:
    def __init__(self, user):
        self._user = user
    
    def generate_payslip(self):
        pass


class Database:
    def __init__(self, user_name, password):
        self._user_name = user_name
        self._password = password
    

    def save_data(self):
        pass

class Notification:
    def __init__(self, user):
        self._user = user
    

    def send_email(self):
        pass
