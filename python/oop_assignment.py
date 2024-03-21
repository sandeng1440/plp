class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"My name is {self.name}. I am a {self.age} year old {self.gender}.")


dude = Person("James", 22, "male")
dude.introduce()
