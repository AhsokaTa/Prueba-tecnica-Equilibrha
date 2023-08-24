import os

class Config:
    """        
    Configuration class to manage settings and environment variables.
    
    This class provides a central location to manage configuration settings for the program.
        
    Attributes:
        file_name (str): The name of the CSV file to load data from.
    """

    def __init__(self):
        self.file_name = os.getenv("file_name", "datos_prueba_tecnica.csv")


"""

"""     
"""
Usar variables de entorno OK, pero siguiente paso es mejorar el archivo config.py 
en formatos como .ini o .json. Para permitir que la configuración se mantenga fuera 
del código fuente y sea más fácil de modificar sin tener que modificar directamente el código. 

"""

