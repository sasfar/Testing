class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point(10,20)
# point1.x = 10
# point1.y = 20
print(point1.x)
# print(point1.y)

# # point2 = Point()
# # point2.x = 30
# # point2.y = 40
# # print(point2.x)
# # print(point2.y)


point1.draw()


    


