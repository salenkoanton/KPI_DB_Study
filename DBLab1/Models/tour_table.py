from .table import Table
from .tour import Tour


class TourTable(Table):

    def __init__(self, objects, filename=None):
        Table.__init__(self, objects, filename)

    def get(self, name=None, id=None):
        if name is not None:
            for obj in self.objects:
                if obj.name == name:
                    return obj
        elif id is not None:
            for obj in self.objects:
                if obj.id == id:
                    return obj

    def create(self, name, place, firm_id):
        tour = Tour(name, place, self.id, firm_id)
        self.id += 1
        self.objects.append(tour)

    def delete(self, obj):
        self.objects.remove(obj)
