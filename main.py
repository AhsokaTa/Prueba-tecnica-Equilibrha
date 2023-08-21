from pandas import read_csv, DataFrame
from config import FILE_NAME

class DataLoader:
    """
    Class for loading data form csv file (FILE_NAME).

    Atributes :
        FILE_NAME (str) :  The csv name to load
    """

    def __init__(self, FILE_NAME):
        """
        Initializes DataLoader instance.
        
        Args:
            FILE_NAME (str): The csv name to load
        """
        self.FILE_NAME = FILE_NAME

    def load_data(self):
        """
        Load data from the CSV file.
        
        Returns:
            DataFrame:  DataFrame with data form csv      
        """
        try:
            data_f = read_csv(self.FILE_NAME, sep=';')
            return data_f
        except Exception as e:
            print("An error occurred during data loading:", str(e))
            raise

class EmployeeHandler:
    """
    A class to handle employees.
    Attributes:
        data_f (DataFrame): The DataFrame containing employee data.
    """

    def __init__(self, data_f):
        """                   
            Initializes the EmployeeHandler instance
        Args:
            data_f (DataFrame): The DataFrame containing employee data.
        """          
        self.data_f = data_f

    def count_gender(self):
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

    def annual_salary(self):
        """
            Calculate the total annual salary of employees.

            Returns:
                float: Containing total annual salary of employees
        """
        try:
            selected_employees = self.data_f[(self.data_f['ID Empresa'] == 1) & (self.data_f['Nombre centro trabajo'] == 'Alovera')]
            tot_salary = selected_employees['salario bruto anual'].sum()

            return tot_salary
        
        except Exception as e:
            print("An error occurred during annual_salary function:", str(e))
            raise

    def get_employees_RRHH(self):
        """
            Get employee data for HR employees with a gross annual salary over 28000.
            Returns:
                DataFrame: Containing employee data for HR employees with a gross annual salary over 28000.
        """
        try:
            selected_employees = self.data_f[(self.data_f['salario bruto anual'] > 28000) & (self.data_f['ID Empresa'] == 2)]
            selected_columns = ['id empleado', 'nombre', 'apellido1', 'apellido2', 'salario bruto anual', 'Nombre empresa']
            select_data = selected_employees[selected_columns]

            return select_data
        
        except Exception as e:
            print("An error occurred during get_employees_RRHH function:", str(e))
            raise
    
    def print_results (self): 
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

if __name__ == "__main__":

    data_loader = DataLoader(FILE_NAME)
    data_f = data_loader.load_data()

    employee = EmployeeHandler(data_f)

    employee.print_results()
    