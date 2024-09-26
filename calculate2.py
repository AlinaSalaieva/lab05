def is_point_in_square(x, y, side_length):
    half_side = side_length / 2
    return (-half_side <= x <= half_side and -half_side <= y <= half_side)

side_length = float(input("Введіть довжину сторони квадрата: "))
point_x = float(input("Введіть координату x точки: "))
point_y = float(input("Введіть координату y точки: "))

if is_point_in_square(point_x, point_y, side_length):
    print("Точка належить квадрату.")
else:
    print("Точка не належить квадрату.")