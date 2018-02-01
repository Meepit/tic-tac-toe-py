class Cell():
    def __init__(self):
        self.available = True
        self.state = ' '

    def is_available(self):
        return self.available

    def get_value(self):
        return self.state

    def change_value(self, value):
        if self.is_available() and value in ['X', 'O']:
            self.state = value
