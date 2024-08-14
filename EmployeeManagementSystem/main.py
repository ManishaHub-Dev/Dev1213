from config import get_db_config

config = get_db_config()
con = mysql.connector.connect(**config)

except mysql.connector.Error as err:
    print(f"Database Error: {err}")
    con.rollback()
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