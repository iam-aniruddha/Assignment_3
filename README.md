### Question 1

Write a decorator to log the following details whenever a function is called:

1. The File needs to be the name of the `<module>_<YYYYMMDD>.log`.
2. The messages in the logs file should follow the format as below:
   - `<module name> <function name> <DD-MM-YY> <hh:mm:ss> <Dict of Arguments passed to the function>`.

### Solution Approach

- Define a decorator `log_decorator` that takes a function as input.
- Within the decorator, define a wrapper function `wrapper` that logs the necessary details.
- Extract the module name, function name, current date, and time.
- Extract the arguments passed to the function and format them into a dictionary.
- Log the details to a file with the specified format.
- Call the original function and return its result.

For the provided solution, the code logs the details of function calls into a file with the specified format whenever a function is called. It utilizes a decorator to achieve this functionality.

---


### Question 2

Write a decorator to log the execution time for a function.

### Solution Approach

- Define a decorator `execution_time_decorator` that takes a function as input.
- Within the decorator, define a wrapper function `wrapper` that records the start time before calling the original function and the end time after the function execution.
- Calculate the execution time by subtracting the start time from the end time.
- Log the execution time along with the module name, function name, and current date to a file.
- Call the original function and return its result.

  The provided solution demonstrates a decorator that calculates and logs the execution time of a function whenever it is called. It's a useful tool for performance analysis and optimization.

---


### Question 3

Write a decorator to validate arguments passed to a function based on a condition. For instance, write a function to generate a sequence of squares of all even numbers in the range of 1 to 10. Check if the number passed as an argument is in the specified range using decorators. If the condition fails, the function should return an exception "ValueError" with an appropriate message.

### Solution Approach

- Define a decorator `validate_range` that takes the minimum and maximum values of the range as input.
- Within the decorator, define another function `decorator` that takes the function to be decorated as input.
- In the `decorator` function, define a wrapper function `wrapper` that checks if the arguments passed to the function are within the specified range.
- If any argument is outside the range, raise a ValueError with an appropriate message.
- Call the original function if all arguments pass the validation.
- Example usage demonstrates how to use this decorator to validate arguments passed to a function.

  The provided solution showcases a decorator that validates arguments passed to a function based on a condition. It's a useful tool for ensuring the correctness of input parameters before executing a function.

---

### Question 4

You are tasked with generating personal details for employees. The goal is to create a dataset of employee records containing the following information:

1. Employee ID
2. Employee Name
3. Employee Email
4. Business Unit
5. Salary

## Solution Approach

In this Python script I accomplishes this task using the `Faker` library. Here's how it works:

1. The `EmployeeData` class is defined, which allows you to specify the number of records to generate (`num_records`) and the file path for saving the data in JSON format (`json_file_path`).
2. The `generate_employee_data` method creates a list of employee records. For each record:

   - An employee ID is generated using a random 6-digit number.
   - The employee's name, email, business unit, and salary are randomly generated using the `Faker` library.
   - The record is added to the list.
3. The `save_to_json` method saves the generated employee data to a JSON file specified by `json_file_path`.

- The `Faker` library (install using `pip install Faker`)

## Usage

1. Clone this repository or download the `EmployeeData.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `EmployeeData.py`.
4. Run the script using `python EmployeeData.py`.

The generated employee data will be saved to the specified JSON file.

---

## Question 5

You are provided with a JSON file containing personal details of employees. Your task is to perform the following operations:

1. **Aggregating Employee Data by Business Unit**:

   - Group employee records based on their business units.
   - Save the aggregated data to a new JSON file.
2. **Terminating Employees**:

   - Delete an employee and their corresponding details when their contract is terminated.
   - Maintain a separate JSON file to store the names of terminated employees.
   - Raise an exception if an attempt is made to delete an employee who is not present in the data.
3. **Salary Hike**:

   - Apply a fixed percentage salary hike for each business unit.
   - Update the salary figures for all employees in the specified business unit.

## Solution Approach

The provided Python script accomplishes the above tasks using the `EmployeeDataManipulator` class. Here's how it works:

1. **Initialization**:

   - The class initializes with the path to the JSON file containing employee data (`json_file_path`).
   - It also initializes empty lists for terminated employees (`terminated_employees`) and an empty dictionary for aggregated data (`aggregated_data`).
2. **Loading Data**:

   - The `load_data` method reads the employee data from the specified JSON file and returns it as a list of dictionaries.
3. **Aggregating by Business Unit**:

   - The `aggregate_by_business_unit` method creates an aggregated dictionary where each business unit is a key.
   - Employee records are grouped under their respective business units.
   - The aggregated data is saved to a new JSON file named "Aggregated_Employee_Data.json".
4. **Deleting Employees**:

   - The `delete_employee` method removes an employee from the data.
   - The employee's name is stored in a separate JSON file named "Terminated_Employees.json".
5. **Applying Salary Hike**:

   - The `apply_salary_hike` method increases the salary of employees in a specified business unit by a given percentage.
6. **Saving Updated Data**:

   - The `save_to_json` method saves the updated employee data to a specified output file.

## Usage

1. Ensure you have the `Employee_Personal_Details.json` file containing employee data.
2. Instantiate the `EmployeeDataManipulator` class.
3. Call the relevant methods (`aggregate_by_business_unit`, `delete_employee`, `apply_salary_hike`, and `save_to_json`) as needed.

we can customize the file paths and adjust the operations according to our requirements.

## Required Dependencies

To run this code, you'll need the following dependencies:

- Python 3.x
- The `Faker` library (install using `pip install Faker`)
