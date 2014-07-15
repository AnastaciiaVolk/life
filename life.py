import random


__author__ = 'Анастасия'


EMPTY_CELL = '.'
ALIVE_CELL = '☻'
WIDTH = 16
HEIGHT = 16


def create_field(width, height):
    a = []
    for i in range(0, width):
        a.append([EMPTY_CELL for j in range(height)])
    return a


def inhebit(a):
    for i in range(0, len(a) - 1):
        for j in range(0, len(a[0]) - 1):
            if random.randint(0, 4) == 0:
                a[i][j] = ALIVE_CELL


def print_field(a):
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            print(a[i][j], end=' ')
        print()


def count_neighbors(a, i, j):
    """
    Количество соседей клетки i,j на поле a
    """
    chet = 0
    i_start = 0 if i == 0 else i-1
    i_end = i if i >= len(a)-1 else i+1
    j_start = 0 if j == 0 else j-1
    j_end = j if j >= len(a[0])-1 else j+1
    for ii in range(i_start, i_end+1):
        for jj in range(j_start, j_end+1):
            if a[ii][jj] == ALIVE_CELL and (i, j) != (ii, jj):
                chet += 1
    return chet


def life(a):
    next_a = create_field(len(a), len(a[0]))
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            cnt = count_neighbors(a, i, j)
            next_a[i][j] = a[i][j]
            if a[i][j] == ALIVE_CELL:
                if cnt>3 or cnt<2:
                    next_a[i][j]= EMPTY_CELL
            elif cnt==3:
                next_a[i][j]=ALIVE_CELL
    return next_a


if __name__ == '__main__':
    a = create_field(20, 20)
    inhebit(a)

    for d in range(0, 10):
        print_field(a)
        print('_' * WIDTH)
        a = life(a)
