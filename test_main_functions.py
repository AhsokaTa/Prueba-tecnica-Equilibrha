import pandas as pd
from main import load_data, count_gender , annual_salary, get_employees_RRHH
from config import FILE_NAME

def test_load_data(): 
    data_frame = load_data(FILE_NAME)    
    #Verify output is a DataFrame
    assert isinstance(data_frame, pd.DataFrame)

def test_count() :
    data = {
        'sexo': ['H', 'H', 'H', 'M', 'M', 'M', 'H','M','H']
    }
    data_frame = pd.DataFrame(data)
    output = (5,4) #Number Men, number Woman
    result = count_gender(data_frame)    
    assert result == output

def test_annual_salary():
    data = {
        'ID Empresa': [1, 1, 1, 1],
        'Nombre centro trabajo': ['Las rozas de Madrid', 'Las rozas de Madrid', 'Alovera', 'Alovera'],
        'salario bruto anual': [21000, 22000, 24000, 25333]
    }
    data_f = pd.DataFrame(data)
    total_expected = 49333  #(24000 + 25333) Sum of the expected gross annual salaries of employees from Alovera
    result = annual_salary(data_f)
    assert result == total_expected



