# The ever changing Ankara: you are a fashion designer known for the unique and vibrant 
# Ankara designs, recently you have discovered that the fabric patterns change there design 
# depending on the temperature and the mood of the wearer. you want to create a software application 
# that predicts the changes in the vibrant designs given the mood and temperature data. think about 
# Python classes you will need to model the changes of Ankara and predict the changes 

class Ankara:
    def __init__(self, temp, mood):
        self.temp = temp
        self.mood = mood

    def predictDesign(self):
        if self.temp >= 20 and self.mood == "happy":
            print("wear less pattern")
        else:
            print("wear more")


ankara = Ankara(20, "cotton")
ankara.predictDesign()



# class Ankara:
#     def __init__(self, temperature, mood):
#         self.temperature = temperature
#         self.mood = mood
#         self.design = None

#     def predict_design(self):
#         if self.temperature >= 30 and self.mood == "happy":
#             self.design = "bright and bold"
#         elif self.temperature > 30 and self.mood == "sad":
#             self.design = "vibrant and cheerful"
#         elif self.temperature < 20 and self.mood == "happy":
#             self.design = "warm and cozy"
#         elif self.temperature < 20 and self.mood == "sad":
#             self.design = "subtle and calming"
#         else:
#             self.design = "classic and elegant"
#         return self.design


# // The magical Baobab: in a small village there is a baobab tree believed to have 
# // magical properties. every season it bears different fruits, each with its own unique power. 
# // you have decided to create a software system that track the changes in the tree and predict 
# // what type of fruit it will bear next season and what it will bear next season and what powers 
# // it will possess. The system should also record the effect of each fruit when consumed. 


class BaobabTree:
    def __init__(self,season, fruit_type, fruit_power):
        self.fruit_seasons = []
        self.season=season
        self.fruit_type=fruit_type
        self.fruit_power=fruit_power
    
    def add_fruit_season(self, season, fruit_type, fruit_power):
        self.fruit_seasons.append((season, fruit_type, fruit_power))
    
    def get_next_fruit_season(self):
        if len(self.fruit_seasons) > 0:
            return self.fruit_seasons[0]
        else:
            return None
    
    def remove_current_fruit_season(self):
        if len(self.fruit_seasons) > 0:
            self.fruit_seasons.pop(0)
    
    def get_all_fruit_seasons(self):
        return self.fruit_seasons
    
    def get_current_fruit_power(self):
        if len(self.fruit_seasons) > 0:
            return self.fruit_seasons[0][2]
        else:
            return None
        