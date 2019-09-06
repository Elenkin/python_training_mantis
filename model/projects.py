from sys import maxsize

class Projects:
    def __init__(self, name=None, status=None, description=None, id=None):
        self.name = name
        self.status = status
        self.description = description
        self.id = id

    #как выглядит строковое представление Объекта выведенного в консоли
    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name, self.status, self.description)

    #сравнение объектов по смыслу (поэлементное сравнение двух списков)
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize