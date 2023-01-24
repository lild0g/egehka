# my_set = {5, 1, 2, 6, 3, 4, 3, 2}
# s = [5, 1, 2, 6, 3, 4, 3, 2]
# print(s)
# my_set.add(4)
# print(my_set)
# my_set.add(4)
# print(my_set, len(my_set), sum(my_set))

# a={} - создание пустого множества

# ТИП а
# print(type(a)) - узнать тип а

# UPDATE
# my_set = {5, 1, 2, 6, 3, 4, 3, 2}
# my_set.add('Hello, World')
# my_set.update((20, 30), [152, 153], {0, -1})
# print(my_set)

# УДАЛЕНИЕ remove(), discard()
# my_set = {5, 1, 2, 6, 3, 4, 3, 2}
# my_set.remove(1)
# my_set.discard(6)
# print(my_set)

# МЕТОД pop() - удаляет случайный элемент
# my_set = {5, 1, 2, 6, 3, 4, 3, 2}
# my_set.remove(1)
# my_set.discard(6)
# a = my_set.pop()
# my_set.clear()
# print(my_set)

# МЕТОД union()
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A | B)
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# C = A | B
# A.union(B)
# B.union(A)
# print(A & B)

# МЕТОД interseption()


# СЛОВАРИ

# пустой словарь
# my_dicts = {}

# словарь с ключами
# my_dicts = {'имя': 'Джон', 1: [2,4,6]}


'''my_dict = dict([[1, 'яблоко'], [2, 'мяч']])
print(my_dict)'''

'''sp = {1: 'яблоко', 2: 'груша', 3: 'апельсин'} # сделать список
   my_dict = dict(sp) # превратить список в словарь
   my_dict[3] = 'мандарин' # добавление элемента
   my_dict[4] = 'слива' # добавление элемента
   my_dict.pop(1) # удаление элемента
   # del my_dict # удаление всего словоря
   print(my_dict.items()) # вывести словарь'''

'''my_dict = {1: 'яблоко', 2: 'груша', 3: 'апельсин'}
   print(my_dict.items())
   print(my_dict.keys())
   print(my_dict.values())'''

# ГЕНЕРАТОР СЛОВАРЕЙ
'''squares = {x: x*x for x in range(6)}
   print(squares)'''

'''squares = {}
   for x in range(6):
     squares[x] = x*x
   print(squares)'''

'''squares = {x: x*x for x in range(10) if x % 2 == 0}
   print(squares)'''

# CTRL+ALT+L - PEP8
