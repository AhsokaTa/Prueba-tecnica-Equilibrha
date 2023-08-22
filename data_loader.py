from pandas import read_csv, DataFrame
from config import FILE_NAME

class DataLoader:
    """
    Class for loading data form csv file (FILE_NAME).

    Atributes :
        FILE_NAME (str) :  The csv name to load
    """

    def __init__(self, FILE_NAME : str):
        """
        Initializes DataLoader instance.
        
        Args:
            FILE_NAME (str): The csv name to load
        """
        self.FILE_NAME = FILE_NAME

    def load_data(self) -> DataFrame:
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