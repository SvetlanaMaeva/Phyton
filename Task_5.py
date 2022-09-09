# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
x_a = int(input('Enter coordinate X: '))
y_a = int(input('Enter coordinate Y: '))
x_b = int(input('Enter coordinate X: '))
y_b = int(input('Enter coordinate Y: '))
distance = ((x_b - x_a) ** 2 + (y_b - y_a) ** 2) ** 0.5
print(f'The distance between two points = {round(distance, 2)}')