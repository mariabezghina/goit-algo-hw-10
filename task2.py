import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x**2

a = 0  # Нижня межа
b = 2  # Верхня межа

n = 100000

x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, max(f(np.linspace(a, b, 1000))), n)

under_curve = y_random < f(x_random)

monte_carlo_area = (b - a) * max(f(np.linspace(a, b, 1000))) * np.sum(under_curve) / n
print(f"Приближене значення інтегралу (метод Монте-Карло): {monte_carlo_area}")

result, error = spi.quad(f, a, b)
print(f"Інтеграл за допомогою quad: {result}, помилка: {error}")

# Побудова графіка функції
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

