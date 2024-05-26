import turtle
import math

# Функція для малювання дерева Піфагора
def draw_pythagoras_tree(t, branch_length, level, angle):
    if level == 0:
        return

    # Малювання стовбура
    t.forward(branch_length)

    # Збереження початкової позиції та кута
    position = t.position()
    heading = t.heading()

    # Малювання правої гілки
    t.right(angle)
    draw_pythagoras_tree(t, branch_length * math.cos(math.radians(angle)), level - 1, angle)

    # Повернення до початкової позиції та кута
    t.setposition(position)
    t.setheading(heading)

    # Малювання лівої гілки
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * math.cos(math.radians(angle)), level - 1, angle)

    # Повернення до початкової позиції та кута
    t.setposition(position)
    t.setheading(heading)

# Основна функція для налаштування екрану та ініціалізації малювання
def main(level):
    # Налаштування екрану
    screen = turtle.Screen()
    screen.title("Pythagoras Tree Fractal")

    # Створення черепашки
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)

    # Виклик функції малювання дерева
    draw_pythagoras_tree(t, 100, level, 45)

    # Приховати черепашку і завершити малювання
    t.hideturtle()
    screen.mainloop()

# Введення рівня рекурсії користувачем
level = int(input("Введіть рівень рекурсії: "))
main(level)
