class Fruits:
    color="orange"
    def __init__(self,color,size,texture):
        self.color=color
        self.size=size
        self.texture=texture

    def change_color(self):
        return f"I ate an {self.color}, {self.size} and {self.texture} fruit"
    def falling(self):
        return f"A {self.size} {self.color} and {self.texture} pawpaw"
    def germinate(self):
        return f"A {self.texture} fruit germinated and its{self.color} and {self.size}"
    



    
