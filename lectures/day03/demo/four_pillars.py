class Hospital:
    pass

class Department:
    
    def __init__(self, head) -> None:
        self.head = head

class Oncology(Department):
    pass

class Employee:
    
    def __init__(self, name, number, pay_grade) -> None:
        pass

    def perform_assigned_task(self):
        pass

class Doctor(Employee):
    pass

    def __init__(self,degree) -> None:
        super().__init__(name, pay_grade)
        self.degree = degree


    def perform_assigned_task(self):
        return super().perform_assigned_task()

class ENT(Doctor):
    pass

class Custodian(Employee):
    pass