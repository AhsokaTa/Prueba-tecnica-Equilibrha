import pandas as pd
from config import FILE_NAME

def load_data (FILE_NAME):
    """Load data from a CSV file into a DataFrame."""
    data_f = pd.read_csv(FILE_NAME, sep=';')    
    print (data_f)

load_data(FILE_NAME)