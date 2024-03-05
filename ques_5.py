"""
# 5. Use the previously created JSON File as an input to the following
# 	a. Create a JSON File to aggregate the above data w.r.t Businees Unit
     and store the Employee details. 
	
# 	b. Delete multiple employee and their corresponding details whenever an employee contract is 
# 	  terminated and maintain the name of the employee in a separate JSON file.
# 	  Raise and exception whenever you are asked to delete the employee details that is not present.

# 	c. Fix a salary hike in terms of percentage for each Business Unit and update the salary figures
# 	for all employees based on the same
"""

import json

class EmployeeDataManipulator:
    """This class is used to manipulate the employee data"""
    def __init__(self, json_file_path="Employee_Personal_Details.json"):
        self.json_file_path = json_file_path
        self.data = self.load_data()
        self.terminated_employees = []
        self.aggregated_data = {}

    def load_data(self):
        """
        Loads employee data from the existing JSON file.
        Returns:
            list: List of dictionaries representing employee records.
        """
        with open(self.json_file_path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)

    def aggregate_by_business_unit(self):
        """
        Aggregates employee data by business unit.
        Returns:
            dict: A dictionary where keys are business units 
            and values are lists of employee records."""

        for emp in self.data:
            business_unit = emp["Business Unit"]
            if business_unit not in self.aggregated_data:
                self.aggregated_data[business_unit] = []
            self.aggregated_data[business_unit].append(emp)
            with open("Aggregated_Employee_Data.json", "w", encoding="utf-8") as output_file:
                json.dump(self.aggregated_data, output_file, indent=4)
        return self.aggregated_data

    def delete_employee(self, emp_name):
        """Deletes an employee from the data."""
        for emp in self.data:
            if emp["EMP NAME"] == emp_name:
                self.data.remove(emp)
                with open("Terminated_Employees.json", "w", encoding="utf-8") as json_file:
                    json.dump(emp_name, json_file, indent=4)
                print(f"Employee {emp_name} terminated and removed from data.")
                return
        raise ValueError(f"Employee {emp_name} not found in the data.")

    def apply_salary_hike(self, business_unit, percentage_increase):
        """Applies a percentage-based salary hike for a specific business unit."""
        for emp in self.data:
            if emp["Business Unit"] == business_unit:
                emp["Salary"] *= (1 + percentage_increase / 100)
        print(f"Salary hike of {percentage_increase}% applied to {business_unit} employees.")

    def save_to_json(self, output_file_path="Updated_Employee_Data.json"):
        """Saves the updated data to a new JSON file."""
        with open(output_file_path, "w", encoding="utf-8") as json_file:
            json.dump(self.data, json_file, indent=4)
        print(f"Updated data saved to {output_file_path}.")

if __name__ == "__main__":
    emp_manipulator = EmployeeDataManipulator()

    # Example usage:
    aggregated_data = emp_manipulator.aggregate_by_business_unit()
    # print(aggregated_data)

    emp_manipulator.delete_employee("Ray Strong")
    emp_manipulator.apply_salary_hike("Engineering", 10)  # 10% salary hike for HR employees

    emp_manipulator.save_to_json()
