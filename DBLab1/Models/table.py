import pickle


class Table:

    def __init__(self, objects, filename=None):
        self.filename = filename
        self.objects = objects
        self.id = 0

    def save(self, filename=None):
        if filename is not None:
            self.filename = filename
        with open(self.filename, 'wb') as file:
            pickle.dump(self, file)

    def load(self, filename=None):
        if filename is not None:
            self.filename = filename
        with open(self.filename, 'rb') as file:
            table = pickle.load(file)
            self.id = table.id
            self.objects = table.objects

    def filter(self, predicate):
        result = []
        for obj in self.objects:
            if predicate(obj):
                result.append(obj)
        return result

