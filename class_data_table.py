from class_items import *


class DataTable:
    def __init__(self, title, columns, data):
        self.title = title
        self.columns = columns
        self.data = data

    def build_table(self):
        # create an array of lines that make up the table display that can be used by other functions to embed into
        # ...other menus, especially the inventory screen!
        pass

    def display_data_table(self):
        # a method to show an example of what the datatable can look like when implemented correctly
        pass


class Column:
    def __init__(self, width, title):
        self.width = width
        self.title = title


def test_data_table():
    dagger = Weapon()
    dagger.name = 'dagger'
    dagger.health = 98
    dagger.cost = 29

    sword = Weapon()
    sword.name = 'sword'
    sword.health = 76
    sword.cost = 48

    table = DataTable(
        'weapons',
        [
            Column(20, 'Item'),
            Column(6, 'Health'),
            Column(4, 'Cost')
        ],
        [
            dagger,
            sword
        ]
    )

    table.display_data_table()


test_data_table()
