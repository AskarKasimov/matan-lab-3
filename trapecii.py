import numpy as np


def calculate_integral_with_error_trapezoidal(a, b, tol):
    def f(x): return np.sin(2 * np.cos(x))

    # оценка максимума второй производной (берем с запасом)
    M2 = 6.0

    # вычисляем необходимое количество разбиений для достижения заданной точности
    h_needed = np.sqrt((12 * tol) / ((b - a) * M2))
    n = int(np.ceil((b - a) / h_needed))

    h = (b - a) / n
    x = np.linspace(a, b, n+1)  # n+1 точек, включая границы отрезка

    # вычисление интеграла методом трапеций
    integral = h/2 * (f(x[0]) + f(x[-1]) + 2 * np.sum(f(x[1:-1])))

    # оценка погрешности по формуле из "справочных сведений"
    error_estimate = (b - a)/12 * h**2 * M2

    return integral, error_estimate, n


result, estimated_error, n_used = calculate_integral_with_error_trapezoidal(
    0, np.pi, 0.00001)

print(f"Приближённое значение интеграла: {result:.10f}")
print(f"Оценка погрешности: {estimated_error:.10f}")
print(f"Использовано разбиений: {n_used}")
