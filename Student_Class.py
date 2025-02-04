class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.marks = [mark1, mark2, mark3]
        self.average = (mark1 + mark2 + mark3) / 3
    
    def average_mark(self):
        return self.average
    
s1 = Student("Pavan",90,90,90)
print(s1.average_mark())