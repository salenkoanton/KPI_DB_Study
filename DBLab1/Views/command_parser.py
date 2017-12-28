import pprint


def get_filename(file):
    print('enter ' + file + ' filename')
    return input()


def get_command():
    return input(">>>")


class Commands:
    GET_COMMAND = 'get'
    CREATE_COMMAND = 'create'
    DELETE_COMMAND = 'delete'
    FROM_STATEMENT = 'from'
    ALL_STATEMENT = 'all'
    WHERE_STATEMENT = 'where'
    FILTER_COMMAND = 'filter'
    SAVE_COMMAND = 'save'
    UPDATE_COMMAND = 'update'


def validate_command(to_parse):
    if to_parse == Commands.GET_COMMAND:
        return to_parse
    elif to_parse == Commands.CREATE_COMMAND:
        return to_parse
    elif to_parse == Commands.DELETE_COMMAND:
        return to_parse
    elif to_parse == Commands.FILTER_COMMAND:
        return to_parse
    elif to_parse == Commands.ALL_STATEMENT:
        return to_parse
    elif to_parse == Commands.SAVE_COMMAND:
        return to_parse
    elif to_parse == Commands.UPDATE_COMMAND:
        return to_parse


def view_data(data):
    pprint.pprint(data.dict(), depth=2, indent=4)


def view_list(data):
    pprint.pprint([item.dict() for item in data], depth=2, indent=4)
