from specialpoints import Specialpoints
import math

def distance_two_point(point1, point2):
    x_square = (point2[0] - point1[0]) ** 2
    y_square = (point2[1] - point1[1]) ** 2
    return math.sqrt(x_square + y_square)

points = [[-3, 1], [2, 2], [-3, 15]]

special_points = Specialpoints(points)

H = special_points.orthorcenter()
O = special_points.circumcenter()
G = special_points.centroid()

if H != None and O != None and G != None:
    print(f"The orthocenter H: {H}\nThe circumcenter O: {O}\nThe centroid G: {G}")
    HG = distance_two_point(H, G)
    HO = distance_two_point(H, O)
    GO = distance_two_point(G, O)
    print(HG / HO)
    print(HG / GO)