import pandas as pd
from config import FILE_NAME

def load_data (FILE_NAME):
    """Load data from a CSV file into a DataFrame."""
    data_f = pd.read_csv(FILE_NAME, sep=';')
    
    return data_f

def count_gender (data_f):
    """Count the number of men and women in the DataFrame."""

    if data_f is not None: 
        cont_men =  (data_f['sexo'] == 'H').sum()
        cont_woman =(data_f['sexo'] =='M').sum()

        return cont_men, cont_woman

def annual_salary (data_f):   
    """Calculate the total annual salary of employees."""

    selected_employees = data_f[(data_f['ID Empresa'] == 1) & (data_f['Nombre centro trabajo'] == 'Alovera')]    
    tot_salary = selected_employees['salario bruto anual'].sum()
    return tot_salary

def get_employees_RRHH(data_f):
    """Get employee data for HR employees with a gross annual salary over 28000."""  

    selected_employees = data_f[(data_f['salario bruto anual'] > 28000) & (data_f['ID Empresa'] == 2)]
    selected_columns = ['id empleado', 'nombre', 'apellido1', 'apellido2', 'salario bruto anual', 'Nombre empresa']
    select_data = selected_employees[selected_columns]
    
    return select_data


data_frame = load_data(FILE_NAME)
count_men, count_women = count_gender(data_frame)
total_salary = annual_salary(data_frame)
employees_hhrr = get_employees_RRHH(data_frame)

print("Number of Men:", count_men)
print("Number of Women:", count_women)
print(f"Total gross annual salary: {total_salary:.2f} €")
print("HR Employees:")

print(employees_hhrr)