from pandas import read_csv, DataFrame
from config import Config

class EmployeeHandler:
    
    """
    A class to handle employees.
    Attributes:
        data_f (DataFrame): The DataFrame containing employee data.
    """
    
    COMPANY_NAME_EQUILIBRHA_RRHH = 2
    WORK_CENTER_ALOVERA = 1
    SALARY_LIMIT = 28000

    def __init__(self, data_f : DataFrame):
        """                   
            Initializes the EmployeeHandler instance
        Args:
            data_f (DataFrame): The DataFrame containing employee data.
        """          
        self.data_f = data_f

    def count_gender(self) -> tuple :
        """
            Count the number of men and women in the DataFrame.
            Returns :
                Tuple : containing the count of men and women in the DataFrame
        """
        try:
            count_of_men = (self.data_f['sexo'] == 'H').sum()
            count_of_women = (self.data_f['sexo'] == 'M').sum()

            return (count_of_men, count_of_women)
        
        except Exception as e:
            print("An error occurred during count_gender function:", str(e))
            raise

    def annual_salary(self) -> float:
        """
            Calculate the total annual salary of employees.

            Returns:
                float: Containing total annual salary of employees
        """
        try:
            selected_employees = self.data_f[(self.data_f['ID Empresa'] == self.WORK_CENTER_ALOVERA) & (self.data_f['Nombre centro trabajo'] == 'Alovera')]
            tot_salary = selected_employees['salario bruto anual'].sum()

            return tot_salary
        
        except Exception as e:
            print("An error occurred during annual_salary function:", str(e))
            raise

    def get_employees_RRHH(self) -> DataFrame:
        """
            Get employee data for HR employees with a gross annual salary over SALARY_LIMIT.
            Returns:
                DataFrame: Containing employee data for HR employees with a gross annual salary over SALARY_LIMIT.
        """
        try:
            selected_employees = self.data_f[(self.data_f['salario bruto anual'] > self.SALARY_LIMIT) & (self.data_f['ID Empresa'] == self.COMPANY_NAME_EQUILIBRHA_RRHH)]
            selected_columns = ['id empleado', 'nombre', 'apellido1', 'apellido2', 'salario bruto anual', 'Nombre empresa']
            select_data = selected_employees[selected_columns]

            return select_data
        
        except Exception as e:
            print("An error occurred during get_employees_RRHH function:", str(e))
            raise
    
    def print_results (self) -> None: 
        """
            Print the analysis results for employees.

            Prints the count of men and women, total gross annual salary and employees who earn more than 28000 and are from the HR department
        """

        count_men, count_women = self.count_gender()
        total_salary = self.annual_salary()
        employees_hhrr = self.get_employees_RRHH()
        print("Number of Men:", count_men)
        print("Number of Women:", count_women)
        print(f"Total gross annual salary: {total_salary:.1f} €")
        print("HR Employees:")
        print(employees_hhrr)