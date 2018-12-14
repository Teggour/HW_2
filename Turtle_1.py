import turtle

turtle.reset()

turtle.speed(3)


def triangle(x1, y1, x2, y2, x3, y3, count):
    if count > 0:
        x12 = (x1 + x2) / 2

        y12 = (y1 + y2) / 2

        x23 = (x2 + x3) / 2

        y23 = (y2 + y3) / 2

        x31 = (x3 + x1) / 2

        y31 = (y3 + y1) / 2

        turtle.pu()

        turtle.goto(x31, y31)

        turtle.pd()

        turtle.goto(x12, y12)

        turtle.goto(x23, y23)

        turtle.goto(x31, y31)

        triangle(x1, y1, x12, y12, x31, y31, count - 1)

        triangle(x2, y2, x12, y12, x23, y23, count - 1)

        triangle(x3, y3, x31, y31, x23, y23, count - 1)


'''Координаты первоначального треугольника'''
point_x_1 = 0

point_y_1 = 200

point_x_2 = 300

point_y_2 = -100

point_x_3 = -300

point_y_3 = -100

'''Количество вложений'''
n = 3

'''Рисунок первоначального треугольника'''
turtle.pu()

turtle.goto(point_x_1, point_y_1)

turtle.pd()

turtle.goto(point_x_2, point_y_2)

turtle.goto(point_x_3, point_y_3)

turtle.goto(point_x_1, point_y_1)

'''Рисунок вложеных треугольников'''
triangle(point_x_1, point_y_1, point_x_2, point_y_2, point_x_3, point_y_3, n)

turtle.exitonclick()