from .table import Table
from .firm import Firm


class FirmTable(Table):

    def __init__(self, objects, tour_table, filename=None):
        Table.__init__(self, objects, filename)
        self.tours = tour_table

    def get(self, name=None, id=None):
        if name is not None:
            for obj in self.objects:
                if obj.name == name:
                    obj.tours = [item.id for item in self.tours.filter(lambda item: item.firm_id == obj.id)]
                    return obj
        elif id is not None:
            for obj in self.objects:
                if obj.id == id:
                    obj.tours = [item.id for item in self.tours.filter(lambda item: item.firm_id == obj.id)]
                    return obj

    def create(self, name):
        firm = Firm(name, self.id)
        self.id += 1
        self.objects.append(firm)

    def delete(self, obj):
        tours = self.tours.filter(lambda item: item.firm_id == obj.id)
        for tour in tours:
            self.tours.delete(tour)
        self.objects.remove(obj)

