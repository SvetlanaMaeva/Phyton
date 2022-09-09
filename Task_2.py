# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
for i in range(0, 8):
    x = i % 2
    y = i // 2 % 2
    z = i // 2 // 2 % 2
    bool_app = not (x or y or z) == ((not x) and (not y) and (not z))
    print(bool_app, z, y, x)