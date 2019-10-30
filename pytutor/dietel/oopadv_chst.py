""" oopadv.py

    Advanced topics in OOP cheat sheet
"""

from decimal import Decimal

class CommissionEmployee:
    def __init__(self, first_name, last_name, ssn, 
                 gross_sales,commission_rate):
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self.gross_sales = gross_sales
        self.commission_rate = commission_rate

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @property
    def gross_sales(self):
        return self._gross_sales

    @gross_sales.setter
    def gross_sales(self, sales):
        if sales < Decimal('0.00'):
            raise ValueError('Gross Sales must be >= 0')
        self._gross_sales = sales
   
    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, rate):
        if not (Decimal('0.00') < rate < Decimal('1.0')):
            raise ValueError('Interest must be between 0 an 1')
        self._commission_rate = rate

    def earnings(self):
        return self.gross_sales * self.commission_rate

    def __repr__(self):
        return (f'CommissionEmployee: ' + 
                f'{self.first_name} {self.last_name}\n' +
                f'social security: {self.ssn}\n' +
                f'gross sales: {self.gross_sales:,.2f}\n' +
                f'commission rate: {self.commission_rate}')

class SalariedCommissionEmployee(CommissionEmployee):
    def __init__(self, first_name, last_name, ssn, gross_sales,
                 commission_rate, base_salary):
        super().__init__(first_name, last_name, ssn, gross_sales, commission_rate)
        self.base_salary = base_salary
    
    @property
    def base_salary(self):
        return self._base_salary
    
    @base_salary.setter
    def base_salary(self, salary):
        if salary < Decimal('0.0'):
            raise ValueError('Base Salary must be >= 0')
        self._base_salary = salary
    
    def earnings(self):
        return super().earnings() + self.base_salary

    def __repr__(self):
        return('Salaried' + super().__repr__() +
               f'\nbase salary: {self.base_salary:,.2f}')


# Duck Typing - if it has the properties it is a duck, you dont need same class

class WellPaidDuck:
    def __repr__(self):
        return 'I am a well-paid duck'
    
    def earnings(self):
        return Decimal('1_000_000.00')

# Operator Overloading - You can overload must of the operators -special methods

class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, right):

        return Complex(self.real + right.real, self.imaginary + right.imaginary)

    def __iadd__(self, right):

        self.real += right.real
        self.imaginary += right.imaginary

        return self

    def __repr__(self):

        return (f'({self.real} ' + 
                  ('+' if  self.imaginary >= 0 else '-') +
                f'{abs(self.imaginary)}i)')
                   


if __name__ == '__main__':
    

    c = CommissionEmployee(first_name='Carlos', last_name='Sell', 
                            ssn='12345', gross_sales=Decimal('10000.00'), 
                            commission_rate=Decimal('0.06'))

    s = SalariedCommissionEmployee(first_name='Carlos', last_name='Sell', 
                            ssn='12345', gross_sales=Decimal('10000.00'), 
                            commission_rate=Decimal('0.06'), 
                            base_salary=Decimal('1000.00'))

    print('SalariedCommissionEmployee is a subclass of CommissionEmployee?',
          f'{issubclass(SalariedCommissionEmployee, CommissionEmployee)}' )   

    print('s is an instance of CommissionEmployee?',
          f'{isinstance(s, CommissionEmployee)}')  

    # Polymorphism with classes with common inheritance 
    d = WellPaidDuck()

    employees = [c,s,d]
    for employee in employees:
        print(employee)
        print(f'{employee.earnings():,.2f}\n') #It will choose the right earnings

    
    x = Complex(real=2, imaginary=4)
    y = Complex(real=5, imaginary=-1)

    print(f'{x} + {y} = {x + y}')
