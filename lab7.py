import numpy as np

def convolution(signal, kernel):
    signal = np.array(signal)
    kernel = np.array(kernel)
    
    signal_len = len(signal)
    kernel_len = len(kernel)

    kernel = kernel[::-1]
    
    output_len = signal_len - kernel_len + 1
    
    result = np.zeros(output_len)

    for i in range(output_len):
        result[i] = np.sum(signal[i:i+kernel_len] * kernel)
    
    return result

signal = [1, 2, 3, 4, 5]
kernel = [1, 0, -1]  

result = convolution(signal, kernel)

print("Результат свёртки:", result)

# Пояснение:
# Сигнал: Это исходные данные, над которыми выполняется операция свёртки.
# Ядро (kernel): Это фильтр, который определяет, как сигнал будет трансформирован.
# Операция свёртки: В каждый момент времени берётся часть сигнала размером с ядро и выполняется поэлементное умножение с ядром. 
# Результаты складываются и сохраняются в выходной массив.
# Инверсия ядра: Ядро нужно инвертировать перед применением свёртки, так как свёртка по определению включает в себя отражение ядра.

# Пример:
# Если сигнал [1, 2, 3, 4, 5] и ядро [1, 0, -1], то свёртка будет работать следующим образом:

# Возьмём первые три элемента сигнала [1, 2, 3] и перемножим их с ядром [1, 0, -1]:
# 1*1 + 2*0 + 3*(-1) = 1 + 0 - 3 = -2

# Сдвинем окно и повторим процесс для следующей тройки [2, 3, 4]:
# 2*1 + 3*0 + 4*(-1) = 2 + 0 - 4 = -2

# И так далее.

# Результат свёртки: [-2, -2, -2].

# Свёртка часто используется в обработке сигналов и изображений для фильтрации или выделения особенностей.