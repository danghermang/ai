import copy
import pprint
pp = pprint.PrettyPrinter(indent=4)


class Table:
    def __init__(self):
        self.matrix = [[1, 1, 1],
                       [0, 0, 0],
                       [-1, -1, -1]]
        self.previous_state = []
        self.next_state = []
        self.level = 0
        self.side = False

    def get_moves(self, x, y):
        if x < 0 or y < 0 or x > len(self.matrix)-1 or y > len(self.matrix)-1:
            return None
        if self.matrix[x][y] == 0:
            return None
        elif self.matrix[x][y] == 1 and self.side:
            results = []
            if x < len(self.matrix)-1:
                if self.matrix[x + 1][y] == 0:
                    results.append((x + 1, y))
                if y != 0 and self.matrix[x + 1][y - 1] == -1:
                    results.append((x + 1, y - 1))
                if y != len(self.matrix)-1 and self.matrix[x + 1][y + 1] == -1:
                    results.append((x + 1, y + 1))
            return results
        elif self.matrix[x][y] == -1 and not self.side:
            results = []
            if x > 0:
                if self.matrix[x - 1][y] == 0:
                    results.append((x - 1, y))
                if y != 0 and self.matrix[x - 1][y - 1] == 1:
                    results.append((x - 1, y - 1))
                if y != len(self.matrix)-1 and self.matrix[x - 1][y + 1] == 1:
                    results.append((x - 1, y + 1))
            return results

    def update_next_steps(self):
        check = False
        lista = []
        for i, row in enumerate(self.matrix):
            for j, element in enumerate(row):
                if element == 1 or element == -1:
                    temp = self.get_moves(i, j)
                    if temp is not None and temp != []:
                        for result in temp:
                            lista.append((i, j, result[0], result[1]))
                            check = True
        # print(lista)
        for element in lista:
            new = copy.deepcopy(self)
            new.next_state = []
            new.previous_state = [self]
            new.level += 1
            if self.side:
                new.side=False
            else:
                new.side=True
            new.move(element[0], element[1], element[2], element[3])
            self.next_state.append(new)
        return check

    def is_draw(self):
        for i, row in enumerate(self.matrix):
            for j, element in enumerate(row):
                if element == 1 or element == -1:
                    if self.get_moves(i, j):
                        return False
        return True

    def is_won(self):
        if not any(-1 in x for x in self.matrix):
            return True
        elif not any(1 in x for x in self.matrix):
            return False
        return None

    def move(self, x1, y1, x2, y2):
        self.matrix[x2][y2] = self.matrix[x1][y1]
        self.matrix[x1][y1] = 0

    def generate_all_steps(self):
        self.update_next_steps()
        lista=[]
        white=[]
        draw=[]
        black=[]
        lista.extend(self.next_state)
        while lista:
            if lista[0].update_next_steps():
                lista.extend(lista[0].next_state)
            # pp.pprint(lista[0].matrix)
            if lista[0].is_won()==True:
                white.append(lista[0])
            elif lista[0].is_won()==False:
                black.append(lista[0])
            elif lista[0].is_draw():
                draw.append(lista[0])
            lista.pop(0)
        return white, black, draw

if __name__ == "__main__":
    table = Table()
    white, black, draw = table.generate_all_steps()
    print('*'*50+"Games won by white"+'*'*50)
    counter=1
    for element in white:
        print("Game "+str(counter))
        temp = element
        lista = []
        while temp.previous_state:
            lista.insert(0, temp.matrix)
            temp=temp.previous_state[0]
        lista.insert(0, temp.matrix)
        for element in lista:
            for row in element:
                print(row)
            print('*' * 10)
        counter += 1
        print('#'*20)
    print('*'*50+"Games won by black"+'*'*50)
    counter = 1
    for element in black:
        print("Game " + str(counter))
        temp = element
        lista = []
        while temp.previous_state:
            lista.insert(0, temp.matrix)
            temp = temp.previous_state[0]
        lista.insert(0, temp.matrix)
        for element in lista:
            for row in element:
                print(row)
            print('*'*10)
        counter += 1
        print('#' * 20)
    print('*'*50+"Draws"+'*'*50)
    counter = 1
    for element in draw:
        print("Game " + str(counter))
        temp = element
        lista = []
        while temp.previous_state:
            lista.insert(0, temp.matrix)
            temp = temp.previous_state[0]
        lista.insert(0, temp.matrix)
        for element in lista:
            for row in element:
                print(row)
            print('*' * 10)
            print('#' * 20)
        counter += 1