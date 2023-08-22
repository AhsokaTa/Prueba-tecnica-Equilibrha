from config import FILE_NAME
from employee_handler import EmployeeHandler
from data_loader import DataLoader

if __name__ == "__main__":

    data_loader = DataLoader(FILE_NAME)
    data_f = data_loader.load_data()

    employee = EmployeeHandler(data_f)

    employee.print_results()

"""
==================================================================
Implementar config.py -> importando os y crear clase Configr
Para ajustar la configuración usando variables de entorno y mejorar
    * Portabilidad
    * Seguridad (sobre todo en entorno de producción)
    * Escalabilidad (desplegar en multiples server)
==================================================================
modulo os (Operating System)
    funciones 
        - os.getenv(var_name , default) :obtener variable de entorno
        - os.path.exists(path) : verifica si un archivo o directoria exist en ruta dada
        - os.listdir(path): Otener lista de archivos y directorios en una ruta.
"""