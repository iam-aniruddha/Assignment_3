"""
# 4. Use the python Faker module to generate fake data for the following.
# 	a. Create an JSON File "Employee Personal Details" with following data.
       Generate around 50-100 records
# 		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"
"""


import json
from faker import Faker

class EmployeeData:
    """
    Generates fake employee data using the Faker library and saves it in a JSON file.

    Args:
        num_records (int, optional): Number of employee records to generate (default is 100).
        json_file_path (str, optional): Path where the employee data will be saved as a JSON file
          (default is "Employee_Personal_Details.json").

    Attributes:
        fake (Faker): An instance of the Faker class.
        num_records (int): Number of employee records to generate.
        json_file_path (str): Path where the employee data will be saved.

    Methods:
        generate_employee_data: Generates fake employee data.
        save_to_json: Saves the generated data to a JSON file.
    """

    def __init__(self, num_records=100, json_file_path="Employee_Personal_Details.json"):
        self.fake = Faker()
        self.num_records = num_records
        self.json_file_path = json_file_path
        self.data = self.generate_employee_data()

    def generate_employee_data(self):
        """Generates fake employee data.
        Returns: List of dictionaries, where each dictionary represents an employee record.
        """
        employee_data = []
        for _ in range(self.num_records):
            emp_id = self.fake.unique.random_number(digits=6)
            emp_name = self.fake.name()
            emp_email = self.fake.email()
            business_unit = self.fake.random_element(elements=('HR', 'Finance', 'Engineering', 'IT', 'Sales', 'Marketing')) # pylint: disable= line-too-long
            salary = self.fake.random_int(min=40000, max=120000)
            employee_record = {
                "EMP ID": emp_id,
                "EMP NAME": emp_name,
                "EMP EMAIL": emp_email,
                "Business Unit": business_unit,
                "Salary": salary
            }
            employee_data.append(employee_record)
        return employee_data

    def save_to_json(self):
        """
        Saves the generated data to a JSON file.
        """
        with open(self.json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(self.data, json_file, indent=4)
        print(f"{self.num_records} records generated and saved to {self.json_file_path}.")

if __name__ == "__main__":
    NUM_RECORDS = 50
    emp_data = EmployeeData(num_records=NUM_RECORDS)
    emp_data.save_to_json()
