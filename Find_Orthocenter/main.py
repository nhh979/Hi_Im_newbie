def vector_two_points(point_1, point_2):
    x = point_2[0] - point_1[0]
    y = point_2[1] - point_1[1]
    return [x, y]

def is_three_points_a_triangle(point_1, point_2, point_3):
    vector_1 = vector_two_points(point_1, point_2)
    vector_2 = vector_two_points(point_1, point_3)

    if (vector_1[0] == vector_2[0] == 0) or (vector_1[1] == vector_2[1] == 0):
        return False
    elif vector_2[0] != 0 and vector_2[1] != 0:
        if vector_1[0] / vector_2[0] == vector_1[1] / vector_2[1]:
            return False
        else:
            return True
    else:
        return True

def altitude(point, vector):
    a = vector[0]
    b = vector[1]
    c = point[0]*a + point[1]*b
    return [a, b, c]

def orthocenter(points):
    A = points[0]
    B = points[1]
    C = points[2]

    if is_three_points_a_triangle(A, B, C):
        #find a altitude AH
        vector_BC = vector_two_points(B, C)
        AH = altitude(A, vector_BC)
        #find another altitude BH
        vector_AC = vector_two_points(A, C)
        BH = altitude(B, vector_AC)

        #find intersection point of two altitudes.
        determinant = AH[0] * BH[1] - AH[1] * BH[0]
        D_bc = BH[1] * AH[2] - AH[1] * BH[2]
        D_ac = BH[2] * AH[0] - AH[2] * BH[0]
        x = D_bc / determinant
        y = D_ac / determinant
        print(f"The orthocenter H: {[x, y]}.")

    else:
        print("Wrong points input. There is no triangle.")

if __name__ == '__main__':
    points = [[10, 0], [-2, 8], [6, 0]]
    orthocenter(points)