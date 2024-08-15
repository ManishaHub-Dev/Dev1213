class Department:
    def __init__(self, id, name, manager_id):
        self.id = id
        self.name = name
        self.manager_id = manager_id
        
class Incentive:
    def __init__(self, id, employee_id, incentive_amount, date_awarded):
        self.id = id
        self.employee_id = employee_id
        self.incentive_amount = incentive_amount
        self.date_awarded = date_awarded