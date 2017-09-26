from Views.command_parser import *


class UI:

    def __init__(self):
        pass

    def filter(self):
        print('enter place')
        place = get_command()
        return place

    def get(self):
        print('enter type firm/tour')
        command = get_command()
        print('enter name or id')
        id = get_command()
        if command == 'firm':
            return command, id
        elif command == 'tour':
            return command, id
        raise Exception('Wrong type identifier')

    def all(self):
        print('enter type firm/tour')
        return get_command()

    def update(self):
        print('enter type firm/tour')
        type = get_command()
        print('enter id')
        id = get_command()
        print('enter name')
        name = get_command()
        if type == 'firm':
            return {
                'type': type,
                'id': id,
                'name': name
            }
        if type == 'tour':
            print('enter place')
            place = get_command()
            print('enter firm id')
            firm_id = int(get_command())
            return {
                'type': type,
                'id': id,
                'name': name,
                'place': place,
                'firm_id': firm_id
            }

    def create(self):
        print('enter type firm/tour')
        type = get_command()
        print('enter name')
        name = get_command()
        if type == 'firm':
            return {
                'type': type,
                'name': name
            }
        if type == 'tour':
            print('enter place')
            place = get_command()
            print('enter firm id')
            firm_id = int(get_command())
            return {
                'type': type,
                'name': name,
                'place': place,
                'firm_id': firm_id
            }
