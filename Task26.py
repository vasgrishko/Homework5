# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def function_degree(a, b):
    if b == 0:
        return 1
    else:
        return a * function_degree(a, b - 1)

print(function_degree(2, 0))
print(function_degree(2, 1))
print(function_degree(2, 3))
print(function_degree(2, 4))