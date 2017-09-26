from .printable import Printable


class Tour(Printable):

    def __init__(self, name, place, id, firm_id):
        Printable.__init__(self)
        self.name = name
        self.place = place
        self.id = id
        self.firm_id = firm_id

    def dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'place': self.place,
            'firm_id': self.firm_id
        }

