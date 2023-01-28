class Man:
    des: str = "Adult"

    def __init__(self, name: str, age: int):
        self.name = name.upper()
        self.age = age

    def speak(self):
        return f"My name is {self.name} and my age is {self.age}"

    def eat(self):
        return "I Am Eating"

    def action(self):
        return "I'm going to office"

    def __repr__(self):
        return f"I am a {self.des} and my name is {self.name}"


class Baby(Man):

    des: str = "Baby"

    def speak(self) -> str:
        return f"Ba ba ba ba na ba"

    def action(self) -> str:
        return f"Pa pa play play"

    def __repr__(self) -> str:
        return f"I am a {self.des} and my name is {self.name}"

