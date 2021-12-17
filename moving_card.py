class moving_card():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y

    def change_pos_x(self, new_pos_x):
        self.pos_x = new_pos_x

    def change_pos_y(self, new_pos_y):
        self.pos_y = new_pos_y
