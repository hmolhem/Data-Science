# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:45:35 2020

@author: Hossein Molhem
"""

import hr

salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
payroll_system = hr.
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])