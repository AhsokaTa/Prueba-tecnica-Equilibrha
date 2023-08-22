from config import FILE_NAME
from employee_handler import EmployeeHandler
from data_loader import DataLoader

if __name__ == "__main__":

    data_loader = DataLoader(FILE_NAME)
    data_f = data_loader.load_data()

    employee = EmployeeHandler(data_f)

    employee.print_results()
