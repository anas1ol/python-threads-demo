import threading
import time
import math

def squares():
    for i in range(1, 6):
        print(f"Потік 1 (квадрати): {i}^2 = {i * i}")
        time.sleep(0.4)   # 400 мс

def cubes():
    for i in range(1, 6):
        print(f"Потік 2 (куби): {i}^3 = {i * i * i}")
        time.sleep(0.5)   # 500 мс

def factorials():
    for i in range(1, 6):
        fact = math.factorial(i)
        print(f"Потік 3 (факторіали): {i}! = {fact}")
        time.sleep(0.6)   # 600 мс

# создаём и запускаем потоки
t1 = threading.Thread(target=squares)
t2 = threading.Thread(target=cubes)
t3 = threading.Thread(target=factorials)

t1.start()
t2.start()
t3.start()

# дожидаемся завершения всех трёх
t1.join()
t2.join()
t3.join()
