import mysql.connector
from report_generator import generate_report

# Database connection
def get_db_config():
    return {
        'host': 'localhost',
        'user': 'root',
        'password': 'password',
        'database': 'emp'
    }

con = mysql.connector.connect(**get_db_config())
cursor = con.cursor()

# Function to check if an employee exists
def check_employee(employee_id):
    sql = 'SELECT * FROM employees WHERE id=%s'
    cursor.execute(sql, (employee_id,))
    return cursor.rowcount == 1

# Step 15: Function to validate salary
def validate_salary(salary):
    try:
        return float(salary) > 0
    except ValueError:
        return False

# Function to add an employee
def add_employee():
    Id = input("Enter Employee Id: ")
    if check_employee(Id):
        print("Employee already exists. Please try again.")
        return
    
    Name = input("Enter Employee Name: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")

    # Step 15: Validate the salary before proceeding
    if not validate_salary(Salary):
        print("Invalid salary. Please try again.")
        return

    sql = 'INSERT INTO employees (id, name, position, salary) VALUES (%s, %s, %s, %s)'
    data = (Id, Name, Post, Salary)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee Added Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to remove an employee
def remove_employee():
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return
    
    sql = 'DELETE FROM employees WHERE id=%s'
    data = (Id,)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee Removed Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to promote an employee
def promote_employee():
    Id = input("Enter Employee's Id: ")
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return
    
    try:
        Amount = float(input("Enter increase in Salary: "))

        sql_select = 'SELECT salary FROM employees WHERE id=%s'
        cursor.execute(sql_select, (Id,))
        current_salary = cursor.fetchone()[0]
        new_salary = current_salary + Amount

        sql_update = 'UPDATE employees SET salary=%s WHERE id=%s'
        cursor.execute(sql_update, (new_salary, Id))
        con.commit()
        print("Employee Promoted Successfully")

    except (ValueError, mysql.connector.Error) as e:
        print(f"Error: {e}")
        con.rollback()

# Function to display all employees
def display_employees():
    try:
        sql = 'SELECT * FROM employees'
        cursor.execute(sql)
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id : ", employee[0])
            print("Employee Name : ", employee[1])
            print("Employee Post : ", employee[2])
            print("Employee Salary : ", employee[3])
            print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to update an employee
def update_employee():
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee does not exist.")
        return
    Name = input("Enter new Employee Name: ")
    Post = input("Enter new Employee Post: ")
    Salary = input("Enter new Employee Salary: ")

    sql = 'UPDATE employees SET name=%s, position=%s, salary=%s WHERE id=%s'
    data = (Name, Post, Salary, Id)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()
        
def add_department():
    id = input("Enter Department Id: ")
    name = input("Enter Department Name: ")
    manager_id = input("Enter Manager Id: ")

    sql = 'INSERT INTO departments (id, name, manager_id) VALUES (%s, %s, %s)'
    data = (id, name, manager_id)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Department added successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()
        
def award_incentive():
    employee_id = input("Enter Employee Id: ")
    incentive_amount = input("Enter Incentive Amount: ")
    date_awarded = input("Enter Date Awarded (YYYY-MM-DD): ")

    sql = 'INSERT INTO incentives (employee_id, incentive_amount, date_awarded) VALUES (%s, %s, %s)'
    data = (employee_id, incentive_amount, date_awarded)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Incentive awarded successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()        

# Function to search employees by salary range
def search_by_salary():
    min_salary = float(input("Enter minimum salary: "))
    max_salary = float(input("Enter maximum salary: "))

    sql = 'SELECT * FROM employees WHERE salary BETWEEN %s AND %s'
    cursor.execute(sql, (min_salary, max_salary))
    employees = cursor.fetchall()

    for employee in employees:
        print(f"Employee Id : {employee[0]}")
        print(f"Employee Name : {employee[1]}")
        print(f"Employee Post : {employee[2]}")
        print(f"Employee Salary : {employee[3]}")
        print("------------------------------------")

# Function to display the menu
def menu():
    while True:
        print("\nWelcome to Employee Management System")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Update Employee")
        print("6 to Search Employees by Salary Range")
        print("7 to Generate Employee Report")
        print("8 to Exit")
        print("9 to Add Department")
        print("10 to Award Incentive")

        choice = input("Enter your Choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            remove_employee()
        elif choice == '3':
            promote_employee()
        elif choice == '4':
            display_employees()
        elif choice == '5':
            update_employee()
        elif choice == '6':
            search_by_salary()
        elif choice == '7':
            generate_report(cursor, 'employee_report.csv')
            print("Report generated successfully")
        elif choice == '8':
            print("Exiting the program. Goodbye!")
        elif choice == '9':
            add_department()
        elif choice == '10':
            award_incentive()
            break
        else:
            print("Invalid Choice! Please try again.")

if __name__ == "__main__":
    menu()
