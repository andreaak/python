"""
Кортежи – это неизменяемые последовательности, обычно используемые,
чтобы хранить разнотипные данные (или однотипные, но логически
представляющие разные сущности). Представлены классом tuple.
"""

# Пустой кортеж
empty_tuple = ()
print(empty_tuple)

# Кортеж из одного элемента
singleton_tuple = (8,)
print(singleton_tuple)

# Кортеж из нескольких элементов
some_tuple = (3, 2, 1, 8)
print(some_tuple)

# Или, что то же самое
some_tuple = 3, 2, 1, 8
print(some_tuple)

# Список кортежей
coordinates = [(8, 3), (2, 0), (3, 4), (0, 0)]
print(coordinates)

# Кортеж кортежей
triangle = ((0, 0), (4, 0), (0, 3))
print(triangle)