# Employee Data Mapping
def map_employee_data(employee_ids, salaries):
    return {employee_ids[i]: salaries[i] for i in range(len(employee_ids))}

# Find the highest salary without built-in functions
def find_highest_salary(data):
    highest_salary = None
    for salary in data.values():
        if highest_salary is None or salary > highest_salary:
            highest_salary = salary
    return highest_salary

# Count employees earning more than a certain amount
def count_high_earners(data, threshold):
    count = 0
    for salary in data.values():
        if salary > threshold:
            count += 1
    return count

# Find the salary of an employee by ID using linear search
def find_salary(data, emp_id):
    for key, value in data.items():
        if key == emp_id:
            return value
    return None

# Main function for Question 1
def question1():
    # Sample input
    employee_ids = [101, 102, 103, 104, 105, 106, 107]
    salaries = [45000, 52000, 61000, 48000, 39000, 72000, 67000]
    employee_data = map_employee_data(employee_ids, salaries)
    
    print("Employee Data:", employee_data)
    
    # (a) Find the highest salary
    highest = find_highest_salary(employee_data)
    print("Highest Salary:", highest)
    
    # (b) Count employees earning more than 50,000
    high_earners = count_high_earners(employee_data, 50000)
    print("Employees earning more than 50,000:", high_earners)
    
    # (c) Find the salary of employee with ID 106
    salary = find_salary(employee_data, 106)
    print("Salary of employee with ID 106:", salary)

# Run Question 1
question1()
