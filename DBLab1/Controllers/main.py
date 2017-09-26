from Controllers.ui import UI
from Models.firm_table import FirmTable
from Models.tour_table import TourTable
from Views.command_parser import *

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Main:

    def __init__(self):
        self.ui = UI()
        self.tours = TourTable([])
        self.firms = FirmTable([], self.tours)

    def init_tables(self):
        self.firms.load(get_filename("firms"))
        self.tours.load(get_filename("tours"))

    def run(self):
        while True:
            command = validate_command(get_command())
            if command == Commands.GET_COMMAND:
                self.get()
            elif command == Commands.DELETE_COMMAND:
                self.delete()
            elif command == Commands.CREATE_COMMAND:
                self.create()
            elif command == Commands.FILTER_COMMAND:
                self.filter()
            elif command == Commands.ALL_STATEMENT:
                self.all()
            elif command == Commands.SAVE_COMMAND:
                self.firms.save()
                self.tours.save()
            elif command == Commands.UPDATE_COMMAND:
                self.update()

    def update(self):
        try:
            input_object = self.ui.update()
            type = input_object['type']
            id = input_object['id']
            obj = None
            if type == 'firm':
                if is_int(id):
                    obj = self.firms.get(id=int(id))
                else:
                    obj = self.firms.get(name=id)
                obj.name = input_object['name']
            elif type == 'tour':
                if is_int(id):
                    obj = self.tours.get(id=int(id))
                else:
                    obj = self.tours.get(name=id)
                obj.name = input_object['name']
                obj.place = input_object['place']
                obj.firm_id = input_object['firm_id']
            view_data(obj)
        except Exception as e:
            print(e.args)

    def get(self):
        try:
            type, id = self.ui.get()
            obj = None
            if type == 'firm':
                if is_int(id):
                    obj = self.firms.get(id=int(id))
                else:
                    obj = self.firms.get(name=id)
            elif type == 'tour':
                if is_int(id):
                    obj = self.tours.get(id=int(id))
                else:
                    obj = self.tours.get(name=id)

            if obj is None:
                raise Exception("can't find " + id)
            view_data(obj)
        except Exception as e:
            print(e.args)

    def filter(self):
        try:
            place = self.ui.filter()
            objects = self.tours.filter(lambda item: item.place == place)
            view_list(objects)
        except Exception as e:
            print(e.args)

    def all(self):
        try:
            type = self.ui.all()
            if type == 'firm':
                view_list(self.firms.objects)
            elif type == 'tour':
                view_list(self.tours.objects)


        except Exception as e:
            print(e.args)

    def delete(self):
        try:
            type, id = self.ui.get()
            obj = None
            if type == 'firm':
                if is_int(id):
                    obj = self.firms.get(id=int(id))
                else:
                    obj = self.firms.get(name=id)
                self.firms.delete(obj)
            elif type == 'tour':
                if is_int(id):
                    obj = self.tours.get(id=int(id))
                else:
                    obj = self.tours.get(name=id)
                self.tours.delete(obj)
            if obj is None:
                raise Exception("can't find " + id)
            view_data(obj)
        except Exception as e:
            print(e.args)

    def create(self):
        try:
            input_object = self.ui.create()
            type = input_object['type']
            if type == 'firm':
                self.firms.create(input_object['name'])
            elif type == 'tour':
                self.tours.create(input_object['name'], input_object['place'], input_object['firm_id'])
            else:
                raise Exception()
        except Exception as e:
            print(e.args)




main = Main()
main.init_tables()
main.run()
#tours = TourTable([])
#firms = FirmTable([], tours)
#firms.create("name")
#tours.create("name", "place", 0)
#firms.save("firms")
#tours.save("tours")
