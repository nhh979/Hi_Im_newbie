class Specialpoints():

    def __init__(self, points):
        self.A = points[0]
        self.B = points[1]
        self.C = points[2]
        if self.is_three_points_a_triangle(self.A, self.B, self.C) == False:
            print('Wrong inputs! Three points do not make a triangle.')

    def middle_points(self, point1, point2):
        return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]

    def vector_two_points(self, point1, point2):
        return [point2[0] - point1[0], point2[1] - point1[1]]

    def line_equation(self, point, vector):
        a = vector[0]
        b = vector[1]
        c = a*point[0] + b*point[1]
        return [a, b, c]

    def intersection_point(self, line1, line2):
        D_ab = line1[0]*line2[1] - line1[1]*line2[0]
        D_ac = line1[0]*line2[2] - line1[2]*line2[0]
        D_cb = line1[2]*line2[1] - line1[1]*line2[2]
        x = D_cb / D_ab
        y = D_ac / D_ab
        return [x, y]

    def is_three_points_a_triangle(self,point_1, point_2, point_3):
        vector_1 = self.vector_two_points(point_1, point_2)
        vector_2 = self.vector_two_points(point_1, point_3)

        if (vector_1[0] == vector_2[0] == 0) or (vector_1[1] == vector_2[1] == 0):
            return False
        elif vector_2[0] != 0 and vector_2[1] != 0 and (vector_1[0] / vector_2[0] == vector_1[1] / vector_2[1]):
            return False
        else:
            return True

    def orthorcenter(self):
        if self.is_three_points_a_triangle(self.A, self.B, self.C):
            #find a altitude
            BC = self.vector_two_points(self.B, self.C)
            AH = self.line_equation(self.A, BC)

            #find another altitude
            AC = self.vector_two_points(self.A, self.C)
            BH = self.line_equation(self.B, AC)

            #return the orthocenter point
            return self.intersection_point(AH, BH)

    def circumcenter(self):
        if self.is_three_points_a_triangle(self.A, self.B, self.C):
            #find a perpendicular bisector
            M = self.middle_points(self.B, self.C)
            vector_BC = self.vector_two_points(self.B, self.C)
            AM = self.line_equation(M, vector_BC)

            #find another perpendicular bisector
            I = self.middle_points(self.A, self.C)
            vector_AC = self.vector_two_points(self.A, self.C)
            BI = self.line_equation(I, vector_AC)

            #return the circumcenter point
            return self.intersection_point(AM, BI)

    def centroid(self):
        if self.is_three_points_a_triangle(self.A, self.B, self.C):
            x = (self.A[0] + self.B[0] + self.C[0]) / 3
            y = (self.A[1] + self.B[1] + self.C[1]) / 3
            return [x, y]