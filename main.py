
from logics import *


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

mas[1][2] = 2
mas[3][0] = 4
print(get_empty_list(mas))

while is_zero_in_mas(mas):
    input()
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num = empty.pop()
    x, y = get_index_from_number(random_num)
    mas = insert_2_or_4(mas, x, y)
    print(f'Мы заполнили элемент под номером {random_num}')
    pretty_print(mas)
