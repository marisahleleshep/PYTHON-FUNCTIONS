class Car:
    tyre=4
    def __init__(self,color,make,model):
        self.make=make
        self.color=color
        self.model=model


    def drive_car(self):
        return f"I drive a {self.model} from {self.make} which is{self.color}"
    def start_car(self):
        return f"I love big{self.model} with grey{self.color} from {self.make}"
  







