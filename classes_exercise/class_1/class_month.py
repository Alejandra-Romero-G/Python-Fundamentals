class Month:
    def __init__(self):
        self.name=""
        self.temp_min = 0
        self.temp_max = 0
    def get_average(self):
        average = (self.temp_max + self.temp_min)/2
        return average
    

