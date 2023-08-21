"""
===========================================================================================================
Encapsulate code into classes. One class for loading data, and another class to handle employee operations.
===========================================================================================================
"""

from pandas import read_csv, DataFrame
from config import FILE_NAME

"""
======================
class for loading data
======================
"""
def load_data (FILE_NAME : str) -> DataFrame : 
    """
    Load data from a CSV file into a DataFrame.
    Args :  
        FILE_NAME (str)
    Returns : 
        DataFrame with data form csv
    """
    try: 
        data_f = read_csv(FILE_NAME, sep=';')     
        return data_f
    except Exception as e :
        print ("An error occurred during load_data function:", str(e))
        raise 

"""
======================
class to handle employee operations
======================
"""
def count_gender (data_f : DataFrame) -> tuple:
    """
    Count the number of men and women in the DataFrame.
    Args : 
        DataFrame (DataFrame) : DataFrame containing employee data
    Returns :
        Tuple : containing the count of men and women in the DataFrame
    """
    
    try :    
        count_of_men = (data_f['sexo'] == 'H').sum() 
        count_of_women = (data_f['sexo'] == 'M').sum()

        return (count_of_men, count_of_women)
    
    except Exception as e :
        print ("An error occurred during count_gender function:", str(e))
        raise

def annual_salary (data_f : DataFrame) -> float:
    """
    Calculate the total annual salary of employees.
    Args : 
        DataFrame (DataFrame) : DataFrame containing employee data
    Returns :
        float: Containing total annual salary of employees 
    """
    try : 
        selected_employees = data_f[(data_f['ID Empresa'] == 1) & (data_f['Nombre centro trabajo'] == 'Alovera')]      
        tot_salary = selected_employees['salario bruto anual'].sum()
        
        return tot_salary
    except Exception as e:
        print("An error occurred during annual_salary function:", str(e))
        raise

def get_employees_RRHH(data_f : DataFrame) -> DataFrame:
    """
    Get employee data for HR employees with a gross annual salary over 28000.
    Args : 
        DataFrame (DataFrame) : DataFrame containing employee data
    Returns:
        DataFrame: Containing employee data for HR employees with a gross annual salary over 28000.
    """
    try : 
        selected_employees = data_f[(data_f['salario bruto anual'] > 28000) & (data_f['ID Empresa'] == 2)]
        selected_columns = ['id empleado', 'nombre', 'apellido1', 'apellido2', 'salario bruto anual', 'Nombre empresa']
        select_data = selected_employees[selected_columns]
        
        return select_data
    except Exception as e :
        print("An error occurred during get_employees_RRHH function:", str(e))
        raise      


data_frame = load_data(FILE_NAME)
count_men, count_women = count_gender(data_frame)
total_salary = annual_salary(data_frame)
employees_hhrr = get_employees_RRHH(data_frame)

print("Number of Men:", count_men)
print("Number of Women:", count_women)
print(f"Total gross annual salary: {total_salary:.2f} €")
print("HR Employees:")
print(employees_hhrr)


"""
def count_gender_version(data_f):
    unique_genders = set(data_f['sexo'])  
    data_f['sexo'].to_list()
    for item in list :
        &%$%&"$%%%    
    return count_of_men, count_of_women

"""
