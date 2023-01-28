# Defining a class

class Students:

    # Class Attribute
    college = "Kiet"
    year = 1

    # Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pass_year(self):
        self.year +=1
        return f"Promoted to {self.year}"


    def __repr__(self):
        return f"{self.name} {self.age}"


s = Students(name="Satyam", age="22")
print(s)
s.college = "MIT"
print(s.college)
s.pass_year()
print(s.year)