class Student:
    def __init__(self, name):
        self.name = name
        self.knowledge = 0
    def study(self):
        self.knowledge += 10
        print(self.name, "is studying")
class Worker:
    def __init__(self):
        self.money = 0
    def work(self):
        self.money += 100
        print("I am working")
class WorkingStudent(Student, Worker):
    def __init__(self, name):
        super().__init__(name)
        Worker.__init__(self)
student = WorkingStudent("Radomyr")
student.study()
student.work()
print("Name:", student.name)
print("Knowledge:", student.knowledge)
print("Money:", student.money)