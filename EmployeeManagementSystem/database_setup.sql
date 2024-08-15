CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES employees(id)
);

CREATE TABLE incentives (
    id INT PRIMARY KEY,
    employee_id INT,
    incentive_amount DECIMAL(10, 2) NOT NULL,
    date_awarded DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);