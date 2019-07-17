from copy import deepcopy
from time import sleep


def field_to_state(table):
    current_state = deepcopy(table)
    for i in range(len(table)):
        for j in range(len(table)):
            cell = current_state[i][j]
            if cell == 0:
                current_state[i][j] = set(range(1, 10))
    return current_state


def finished(current_state):
    for row in current_state:
        for cell in row:
            if isinstance(cell, set):
                return False
    return True


def print_solution(table):
    if not table:
        print("No solution")
        return
    sleep(0.2)
    print("■" * 19)
    for i in range(len(table)):
        print('■ ', end='')
        for j in range(len(table)):
            cell = table[i][j]
            if cell == 0 or isinstance(cell, set):
                print('.', end='')
            else:
                print(cell, end='')
            if (j + 1) % 3 == 0 and j < 8:
                print(' ■', end='')
            if j != 8:
                print(' ', end='')
        print(' ■', end='')
        print('\n', end='')
        if (i + 1) % 3 == 0 and i < 8:
            print("■" * 19)
    print("■" * 19)


def compute_step(current_state):
    print('Step')
    print_solution(current_state)
    modifications = False
    for i in range(len(table)):
        row = current_state[i]
        values = set([x for x in row if not isinstance(x, set)])
        for j in range(len(table)):
            if isinstance(current_state[i][j], set):
                current_state[i][j] -= values
                if len(current_state[i][j]) == 1:
                    current_state[i][j] = current_state[i][j].pop()
                    modifications = True
                elif len(current_state[i][j]) == 0:
                    return False, None
    for j in range(len(table)):
        column = [current_state[x][j] for x in range(len(table))]
        values = set([x for x in column if not isinstance(x, set)])
        for i in range(len(table)):
            if isinstance(current_state[i][j], set):
                current_state[i][j] -= values
                if len(current_state[i][j]) == 1:
                    current_state[i][j] = current_state[i][j].pop()
                    modifications = True
                elif len(current_state[i][j]) == 0:
                    return False, None
    for x in range(3):
        for y in range(3):
            values = set()
            for i in range(3*x, 3*x+3):
                for j in range(3*y, 3*y+3):
                    cell = current_state[i][j]
                    if not isinstance(cell, set):
                        values.add(cell)
            for i in range(3*x, 3*x+3):
                for j in range(3*y, 3*y+3):
                    if isinstance(current_state[i][j], set):
                        current_state[i][j] -= values
                        if len(current_state[i][j]) == 1:
                            current_state[i][j] = current_state[i][j].pop()
                            modifications = True
                        elif len(current_state[i][j]) == 0:
                            return False, None
    return True, modifications


def compute_state(current_state):
    while True:
        solvable, modifications = compute_step(current_state)
        if not solvable:
            return False
        if not modifications:
            return True


def forward_check(current_state):
    solvable = compute_state(current_state)
    if not solvable:
        return None
    if finished(current_state):
        return current_state
    for i in range(len(table)):
        for j in range(len(table)):
            cell = current_state[i][j]
            if isinstance(cell, set):
                for value in cell:
                    new_state = deepcopy(current_state)
                    new_state[i][j] = value
                    solved = forward_check(new_state)
                    if solved is not None:
                        return solved
                return None

table = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 0],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]
print('First table')
print_solution(table)
state = field_to_state(table)
final = forward_check(state)
print('Final solution:')
print_solution(final)