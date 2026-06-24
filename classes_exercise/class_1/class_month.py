#I used a class to group related data and behavior together. 
# The __init__ method initializes the object's attributes when a new instance is created. 
# The self parameter refers to the current object and allows access to its attributes. 
# The get_average() method calculates and returns the average temperature. This approach 
# makes the code more organized and reusable.
class Month:
    def __init__(self):
        self.name=""
        self.temp_min = 0
        self.temp_max = 0
    def get_average(self):
        average = (self.temp_max + self.temp_min)/2
        return average
    

