import numpy as np
import matplotlib.pyplot as plt

def plot_polynomial(expression, x_min, x_max):
    x_val = np.linspace(x_min, x_max, 200)

    y_val = np.array([eval(expression) for x in x_val])

    plt.plot(x_val, y_val)
    plt.title(f'Wykres funkcji: {expression}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

expression = input("Podaj wielomian f(x): ")
x_min = float(input("Podaj x_min: "))
x_max = float(input("Podaj x_max: "))

plot_polynomial(expression, x_min, x_max)
