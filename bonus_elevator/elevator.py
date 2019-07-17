
class Elevator:
    def __init__(self,floors=5,max_weight=1000):
        self.current_floor = 0
        self.current_weight = 0
        self.max_floor=floors
        self.max_weight=max_weight
        self.direction = None
        self.commands=[]

    def add_command(self,floor,direction):
        if floor<0 or floor>self.max_floor:
            self.commands.append((floor,direction))
            if self.direction:
                self.commands.sort(key=custom_sort_up)
            else:
                self.commands.sort(key=custom_sort_down)

    def do_next_command(self):

def custom_sort_up(first,second):
    if first[1] and second[1]:
        if first[0]<second[0]:
            return 1
        else:
            return -1
    elif not first[1] and not second[1]:
        if first[0]>second[0]:
            return 1
        else:
            return -1
    elif first[1] and not second[1]:
        return 1
    else:
        return -1


def custom_sort_down(first,second):
    return -custom_sort_up(first,second)

