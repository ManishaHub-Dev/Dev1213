import csv

def generate_report(cursor, file_name):
    sql = 'SELECT * FROM employees'
    cursor.execute(sql)
    rows = cursor.fetchall()

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Name', 'Post', 'Salary'])
        writer.writerows(rows)