class Period:
    #время в секундах
    first_moment=None
    second_moment=None
    def __init__(self, first_moment, second_moment):
        self.first_moment = first_moment
        self.second_moment = second_moment
    
    def get_dif_moment(self):
        return self.second_moment - self.first_moment

    def get_dif_moment_from_minutes(self):
        return (self.second_moment - self.first_moment) / 60
    
    def get_dif_moment_from_hours(self):
        return (self.second_moment - self.first_moment) / 60 / 60
    
    def get_dif_moment_from_days(self):
        return (self.second_moment - self.first_moment) / 60 / 60 / 24