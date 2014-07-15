MAX_QUAD_SIZE = 10

__author__ = 'Анастасия'


class MapQuad:
    def __init__(self, field, parent, x1, y1, x2, y2):
        self.field = field
        self.parent = parent
        self.size = x2-x1+1
        self.cell_count = ?
        self.children = [None] * 4
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if self.size > MAX_QUAD_SIZE:
            self.children = []
            x_middle = x1+self.size/2
            y_middle = y1+self.size/2
            self.children.append(MapQuad(field, self, x1, y1, x_middle, y_middle))
            self.children.append(MapQuad(field, self, x_middle+1, y1, x2, y_middle))
            self.children.append(MapQuad(field, self, x1, y_middle+1, x_middle, y2))
            self.children.append(MapQuad(field, self, x_middle+1, y_middle+1, x2, y2))

            self.cell_count = sum([c.cell_count for c in self.children])
        else:
            self.cell_count = self.count_cells()

    def count_cells(self):
        cnt = 0
        for i in range(self.x1, self.x1+1):
            for j in range(self.y1, self.y1+1):
                if self.field[j][i] != '.':
                    cnt += 1
        return cnt



def create_quad_from_field(field):
    result = MapQuad(field, None, 0, 0, len(field)-1, len(field[0])-1)

