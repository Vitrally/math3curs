import numpy as np

def fft(x):
    N = len(x)
    if N <= 1:
        return x

    even = fft(x[::2])
    odd = fft(x[1::2])
    
    T = [np.exp(-2j * np.pi * k / N) * odd[k % (N // 2)] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def ifft(x):
    N = len(x)
    if N <= 1:
        return x

    even = ifft(x[::2])

    odd = ifft(x[1::2])
    
    
    T = [np.exp(2j * np.pi * k / N) * odd[k % (N // 2)] for k in range(N // 2)]
    return [(even[k] + T[k]) / 2 for k in range(N // 2)] + [(even[k] - T[k]) / 2 for k in range(N // 2)]

def convolve(x, y):
    N = len(x) + len(y) - 1
    # Zero-padding to the next power of 2 for efficiency
    N = 1 << (N - 1).bit_length()
    
    X = np.pad(x, (0, N - len(x)), 'constant')
    Y = np.pad(y, (0, N - len(y)), 'constant')
    
    X_fft = fft(X)
    Y_fft = fft(Y)
    
    Z_fft = [X_fft[i] * Y_fft[i] for i in range(N)]
    
    Z = ifft(Z_fft)
    return np.real(Z[:len(x) + len(y) - 1])

# Пример использования
x = [1, 2, 3]

y = [4, 5, 6, 7, 8]

result = convolve(x, y) 
print(result)









































'''

import numpy as np

def fft(x):
    N = len(x)  # Получаем длину входного массива x
    if N <= 1:  # Если длина 1 или меньше, возвращаем x
        return x

    even = fft(x[::2])  # Рекурсивно вызываем fft для четных индексов
    odd = fft(x[1::2])   # Рекурсивно вызываем fft для нечетных индексов
    
    # Вычисляем преобразование Фурье для нечетных индексов с использованием формулы
    T = [np.exp(-2j * np.pi * k / N) * odd[k % (N // 2)] for k in range(N // 2)]
    
    # Собираем результат, комбинируя четные и нечетные части
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def ifft(x):
    N = len(x)  # Получаем длину входного массива x
    if N <= 1:  # Если длина 1 или меньше, возвращаем x
        return x

    even = ifft(x[::2])  # Рекурсивно вызываем ifft для четных индексов
    odd = ifft(x[1::2])   # Рекурсивно вызываем ifft для нечетных индексов
    
    # Вычисляем преобразование Фурье для нечетных индексов с использованием обратной формулы
    T = [np.exp(2j * np.pi * k / N) * odd[k % (N // 2)] for k in range(N // 2)]
    
    # Собираем результат, комбинируя четные и нечетные части с делением на 2
    return [(even[k] + T[k]) / 2 for k in range(N // 2)] + [(even[k] - T[k]) / 2 for k in range(N // 2)]

def convolve(x, y):
    N = len(x) + len(y) - 1  # Определяем длину выходного массива
    N = 1 << (N - 1).bit_length()  # Выравниваем длину до ближайшей степени двойки для эффективности
    
    X = np.pad(x, (0, N - len(x)), 'constant')  # Дополняем x нулями до длины N
    Y = np.pad(y, (0, N - len(y)), 'constant')  # Дополняем y нулями до длины N
    
    X_fft = fft(X)  # Применяем FFT к x
    Y_fft = fft(Y)  # Применяем FFT к y
    
    Z_fft = [X_fft[i] * Y_fft[i] for i in range(N)]  # Перемножаем преобразования Фурье
    
    Z = ifft(Z_fft)  # Применяем обратное преобразование Фурье
    return np.real(Z[:len(x) + len(y) - 1])  # Возвращаем действительную часть результата с нужной длиной

# Пример использования
x = [1, 2, 3]  # Первый массив
y = [4, 5, 6, 7, 8]  # Второй массив

result = convolve(x, y)  # Выполняем свертку
print(result)  # Выводим результат
'''