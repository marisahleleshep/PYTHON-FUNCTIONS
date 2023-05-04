class Student:
    name="Emily"
    age=21
    school="AkiraChix"
    nationality="Kenyan"
    first_name="Marisah"
    last_name="Kevin"
    country="Rwanda"


class Student:
    school="AkiraChix"
    def __init__(self,name,age,nationality,first_name,last_name,country):
        self.name=name
        self.age=age
        self.nationality=nationality
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country



    def greet_student(self):
        return f"Hello {self.name},welcome to {self.school}, I am a proud {self.nationality}"

    def show_full_name(self):
        return f"Hello my name is{self.first_name} {self.last_name}"
    
    def year_of_birth(self):
        return f"I was born in the year {self.year_of_birth}"
    
    def show_initial(self):
        return f"{self.first_name[0]}.{self.last_name[0]}" 




