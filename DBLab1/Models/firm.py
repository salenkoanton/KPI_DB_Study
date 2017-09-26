from .printable import Printable


class Firm(Printable):

    def __init__(self, name, id):
        Printable.__init__(self)
        self.name = name
        self.id = id
        self.tours = None

    def dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'tours': self.tours
        }
