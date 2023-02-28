class entity:
    def __init__(self, x, y, x_speed=0, y_speed=0):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def log(self):
        print(f"position: [{self.y}, {self.x}]")
        print(f"Velocity: [{self.y_speed}, {self.x_speed}]")
