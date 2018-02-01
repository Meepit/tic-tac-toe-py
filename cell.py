class Cell():
    def __init__(self):
        self.available = False
        self.state = ' '

    def is_available(self):
        return self.available

    def get_value(self):
        return self.state
