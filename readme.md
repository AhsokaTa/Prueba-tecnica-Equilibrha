# Equilibrha Technical Test

This program processes a CSV file containing employee data. Once the data is loaded into memory, it performs various operations on it.

## Features

1. **Gender Count:**
   The program counts the number of men and women among the total employees.

2. **Sum of Salaries (Company 1, Work Center CT2):**
   It calculates the sum of the gross annual salary of employees from company 1 (Equilibra IT) and work center CT2 (Alovera).

3. **List of Relevant Employees (Company 2, Salary > 28000):**
   It prints a list of employees who earn more than 28000 euros and belong to company 2 (Equilibra RRHH). It displays their ID, name, last name, salary, and company.

## Dependency Installation

### Windows

1. Create a Python environment:
    ```
    python -m venv environment
    ```

2. Activate the environment:
    ```
    environment\Scripts\activate
    ```

3. Install the requirements:
    ```
    pip install -r requirements.txt
    ```

### macOS y Linux

1. Create a Python environment:
    ```
    python3 -m venv environment
    ```

2. Activate the environment:
    ```
    source environment/bin/activate
    ```

3. Install the requirements:
    ```
    pip3 install -r requirements.txt
    ```

# Run the program
# Windows 
```
python main.py
```
# macOS y Linux
```
python3 main.py
```

# Unit Test
To execute the unit tests, write "pytest" in the command line.
```
pytest
```