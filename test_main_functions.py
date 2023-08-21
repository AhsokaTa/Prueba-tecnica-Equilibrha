import pandas as pd
from main import DataLoader, EmployeeHandler
from config import FILE_NAME

def test_load_data():
    data_loader = DataLoader(FILE_NAME)
    data_f = data_loader.load_data()
    assert isinstance(data_f, pd.DataFrame)

def test_count_gender():
    data = {
        'sexo': ['H', 'H', 'H', 'M', 'M', 'M', 'H', 'M', 'H']
    }
    data_f = pd.DataFrame(data)
    employee_handler = EmployeeHandler(data_f)
    result = employee_handler.count_gender()
    assert result == (5, 4)

def test_annual_salary():
    data = {
        'ID Empresa': [1, 1, 1, 1],
        'Nombre centro trabajo': ['Las rozas de Madrid', 'Las rozas de Madrid', 'Alovera', 'Alovera'],
        'salario bruto anual': [21000, 22000, 24000, 25333]
    }
    data_f = pd.DataFrame(data)
    employee_handler = EmployeeHandler(data_f)
    total_expected = 49333
    result = employee_handler.annual_salary()
    assert result == total_expected