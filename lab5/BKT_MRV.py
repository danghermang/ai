import copy


def field_to_state(table):
    current_state = copy.deepcopy(table)
    for i in range(len(table)):
        for j in range(len(table)):
            cell = current_state[i][j]
            if cell == 0:
                current_state[i][j] = set(range(1,10))
    return current_state


def compute_state(current_state):
    modifications = False
    for i in range(len(current_state)):
        row = current_state[i]
        values = set([val for val in row if not isinstance(val, set)])
        for j in range(len(current_state)):
            if isinstance(current_state[i][j], set):
                current_state[i][j] -= values
    for j in range(len(current_state)):
        column = [current_state[x][j] for x in range(len(current_state))]
        values = set([val for val in column if not isinstance(val, set)])
        for i in range(len(current_state)):
            if isinstance(current_state[i][j], set):
                current_state[i][j] -= values
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
    min_i, min_j = -1, -1
    min_domain_length = 100
    for i in range(len(current_state)):
        for j in range(len(current_state)):
            if isinstance(current_state[i][j], set):
                domain_length = len(current_state[i][j])
                if min_domain_length > domain_length > 0:
                    min_domain_length = domain_length
                    min_i = i
                    min_j = j
    if isinstance(current_state[i][j], set):
        current_state[min_i][min_j] = current_state[min_i][min_j].pop()
        modifications = True
    return True, modifications


def print_solution(table):
    if not table:
        print("No solution")
        return
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


def forward_checking(current_State):
    while True:
        print('Step')
        print_solution(current_State)
        solvable, changes_made = compute_state(current_State)
        if not solvable:
            return False
        if not changes_made:
            return True    


def finished(current_state):
    for row in current_state:
        for cell in row:
            if isinstance(cell, set):
                return False
    return True


def bkt_mrv(init_state):
    current_state = field_to_state(init_state)
    result = forward_checking(current_state)
    if not result:
        return None
    if finished(current_state):
        return current_state
    for i in range(len(current_state)):
        for j in range(len(current_state)):
            cell = current_state[i][j]
            if isinstance(cell, set):
                for value in cell:
                    new_table = copy.deepcopy(current_state)
                    new_table[i][j] = value
                    result = bkt_mrv(new_table)
                    if result is not None:
                        return result
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
final = bkt_mrv(table)
print('Final solution:')
print_solution(final)
