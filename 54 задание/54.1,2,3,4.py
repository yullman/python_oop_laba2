class Rectangle:
    width=None
    height=None
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get1(self):
        return self.width * self.height
    
    def get2(self):
        return 2 * self.width + 2 * self.height
    
    def get3(self):
        return self.get_s() / self.get_p()