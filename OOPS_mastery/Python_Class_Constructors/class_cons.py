class Point:

    def __new__(cls, *args, **kwargs):
        print("1 created a new instance of point")
        return super().__new__(cls)

    def __init__(self, x, y):
        print("2. Initialize the new instance o0f point")
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y})"