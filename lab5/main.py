class Graph:
    def __init__(self, countries, colours, ties):
        self.countries = countries
        self.colours_of_countries = dict()
        self.colours = colours
        self.ties = dict()
        for index in countries:
            self.colours_of_countries[index] = colours
            self.ties[index] = []
        for index in ties:
            vector = index.split()
            if len(vector) > 1:
                for i in vector[1:]:
                    self.ties[vector[0]].append(i)
countries = []
f = open('adjacent-states', 'r')
element = f.read()
element.replace('\n', ' ')
for piece in element.split():
    if piece not in countries:
        countries.append(piece)
countries.sort()
f.close()
colours = ['Red', 'Green', 'Blue']
f = open('adjacent-states', 'r')
ties = []
element = f.read()
for piece in element.split('\n'):
    if piece not in ties:
        ties.append(piece)
ties.sort()
f.close()
a = Graph(countries, colours, ties)

print(a.colours_of_countries)
print(a.ties)
