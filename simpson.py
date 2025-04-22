import numpy as np


def calculate_integral_with_error_simpson(a, b, tol):
    def f(x): return np.sin(2 * np.cos(x))

    # оценка максимума четвертой производной (берем с запасом)
    M4 = 100.0

    # вычисляем необходимое количество разбиений для достижения заданной точности
    h_needed = ((180 * tol) / ((b - a) * M4))**(1/4)
    n = 2 * int(np.ceil((b - a) / (2 * h_needed)))  # n должно быть четным
    if n % 2 != 0:
        n += 1  # убедимся, что n четное

    h = (b - a) / n
    x = np.linspace(a, b, n+1)  # n+1 точек, включая границы отрезка

    # вычисление интеграла методом Симпсона
    integral = h/3 * (f(x[0]) + f(x[-1]) +
                      # нечетные индексы (x1, x3, ...)
                      4 * np.sum(f(x[1:-1:2])) +
                      # четные индексы (x2, x4, ...)
                      2 * np.sum(f(x[2:-1:2])))

    # оценка погрешности по формуле из "справочных сведений"
    error_estimate = (b - a)/180 * (h**4) * M4

    return integral, error_estimate, n


result, estimated_error, n_used = calculate_integral_with_error_simpson(
    0, np.pi, 0.00001)

print(f"Приближённое значение интеграла: {result:.10f}")
print(f"Оценка погрешности: {estimated_error:.10f}")
print(f"Использовано разбиений: {n_used}")
