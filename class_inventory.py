from class_items import *

# list.index(X). Returns the index in the list of the first item whose value...
# ...is x. It is an error if there is no such item.
# list.count(X). Returns the number of times x appears in the list.


class Container:
    """Class for physical containers or character inventories"""

    TYPE = 'Container'
    
    def __init__(self, pos_x=0, pos_y=0, inventory=0):
        self.name = 'Container'
        self.key = 'U'
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.keyLevel = 1
        self.inventory = inventory  # Record of an inventory.

    def read_attributes(self, file):
        file_name = 'Assets/Entities/{0}'.format(file)
        # RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE
        # RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE
        # RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE#RE-WRITE
        
        # valid_attribs = ['NAME', 'TYPE', 'KEY ', 'POSX', 'POSY', 'KLVL', 'INVY']
        # f = open(file_name, 'r')
        # print('  |Reading Container file: ', file_name)#
        #
        # This loop decodes each attribute and value line by line in the file.
        # for line in f:
        #    reading = True
        #    try:
        #        attrib = line[0] +line[1] +line[2] +line[3]
        #        print('  |{0}'.format(attrib))#
        #    except IndexError:
        #        print('  |Error: Line With No Named Attribute.')#
        #        reading = False
        #
        #    # This loop reads the value of valid attributes.
        #    if reading and (attrib in valid_attribs):
        #        value = []
        #        for i in range(5, len(line) - 1):
        #            value.append(line[i]) # Reads value excluding \n.
        #        value = ''.join(value) # Stringifes value.
        #        print('  | ', value)#

        file_type = get_file_type(file)
        data = get_file_attribs(file_name, file_type)
        attrib = data[0]
        value = data[1]

        for i in range(len(attrib)):
            # Assigning values to the attribute addressed in the read loop.
            if attrib[i] == 'NAME':
                self.name = value[i]
            # TYPE is automatically assigned to Container for all containers.
            elif attrib[i] == 'KEY ':
                self.key = value[i]
            # PosX and Y values ignored to allow peramiter overide.
            elif attrib[i] == 'KLVL':
                self.keyLevel = int(value[i])
            elif attrib[i] == 'INVY':
                self.inventory = value[i]
            # Last value gets ignored without returning at the end.
            # Make sure each txt file has an empty line at the end.
        
        print('  |File: "{0}" Processed!'.format(file_name))


class Inventory:
    def __init__(self):
        # Separating items into categories/item types
        self.name = 'Inventory'
        self._capacity = 100
        
        self._weapons = []
        self._consumables = []
        self._armour = []
        self._notes = []
        self.keys = []
        self._unsorted = []

    def read_attributes(self, file_name):
        file_lines = get_file_lines(file_name)

        # Reads the name and the capacity of the inventory.
        print('    |Reading Inventory File: {0}'.format(file_name))
        self.name = file_lines[0]
        print('    |NAME\n    |  {0}'.format(self.name))
        self._capacity = file_lines[1]
        print('    |CAP \n    |  {0}'.format(self._capacity))
        
        # Reads the name(not directory) of the file containing the item data.
        items = []
        item = None
        for i in range(2, len(file_lines)):
            item = file_lines[i]
            print('    |{0}'.format(item))
            items.append(item)

        # Read the item file and add the item to the inventory.

        for i in range(len(items)):
            if items[i][0] == 'I':
                item = Item()
            elif item[i][0] == 'W':
                item = Weapon()
            elif item[i][0] == 'A':
                item = Armour()
            elif item[i][0] == 'E':
                item = Consumable()
            elif item[i][0] == 'N':
                item = Note()
            elif item[i][0] == 'K':
                item = Key()

            # Had the idea to create a single read function to do all this for me...

            # item.read_attributes(items[i])# Not Yet Completed

    def add_item(self, item):
        self.sort_item(item)

    def sort_item(self, item):
        if item.TYPE == "Weapon":
            self._weapons.append(item)
        elif item.TYPE == "Consumable":
            self._consumables.append(item)
        elif item.TYPE == "Armour":
            self._armour.append(item)
        elif item.TYPE == "Note":
            self._notes.append(item)
        elif item.TYPE == "Key":
            self.keys.append(item)
        else:
            self._unsorted.append(item)

    # def search_inv(self, name):  # WTF IS THIS SHIT!! DO IT PROPERLY!!
    #     # Returns the index of the item,  or False if no item found.
    #     found = False
    #     for cat in range(len(self._all)):
    #         for item in range(len(category[cat][item])):
    #             if self._all[cat][item].name == str(name):
    #                 found = True
    #                 return self._all.index(cat, item)  #probs dosent work#
    #             else:
    #                 pass
    #     if not found:
    #         return False

    def show_inv(self):
        all_inv = []
        select = '   '  # Added before each item in the table before selected.

        all_inv.append('|--------------------------------------------------------|')
        all_inv.append('|Unsorted                     |Value|Weight|             |')
        for i in range(len(self._unsorted)):
            item = self._unsorted[i]
            all_inv.append('|{0}: {1:<24}|{2:>5}|{3:>6}|             |'.format(select, item.name, item.value, item.weight))
        all_inv.append('|--------------------------------------------------------|')
        all_inv.append('|Weapons                      |Value|Weight|Health|Damage|')
        for i in range(len(self._weapons)):
            item = self._weapons[i]
            all_inv.append('|{0}: {1:<24}|{2:>5}|{3:>6}|{4:>6}|{5:>6}|'.format(select, item.name, item.value, item.weight, item.health, item.damage))
        all_inv.append('|--------------------------------------------------------|')
        all_inv.append('|Armour                       |Value|Weight|Health|Defnce|')
        for i in range(len(self._armour)):
            item = self._armour[i]
            all_inv.append('|{0}: {1:<24}|{2:>5}|{3:>6}|{4:>6}|{5:>6}|'.format(select, item.name, item.value, item.weight, item.health, item._defence))
        all_inv.append('|--------------------------------------------------------|')
        all_inv.append('|Consumables                  |Value|Weight|Effect|      |')
        for i in range(len(self._consumables)):
            item = self._consumables[i]
            all_inv.append('|{0}: {1:<24}|{2:>5}|{3:>6}|{4:>6}|      |'.format(select, item.name, item.value, item.weight, 'NoDisp'))
        all_inv.append('|--------------------------------------------------------|')
        all_inv.append('|Notes                        |Value|Weight|Sectns|      |')
        for i in range(len(self._notes)):
            item = self._notes[i]
            all_inv.append('|{0}: {1:<24}|{2:>5}|{3:>6}|{4:>6}|      |'.format(select, item.name, item.value, item.weight, len(item._headers)))
        all_inv.append('|--------------------------------------------------------|')
        all_inv.append('|Keys                         |Value|Weight|             |')
        for i in range(len(self.keys)):
            item = self.keys[i]
            all_inv.append('|{0}: {1:<24}|{2:>5}|{3:>6}|             |'.format(select, item.name, item.value, item.weight))
        
        # for each in all_inv:
            # print(each)

        mod_x = 0
        running = True
        while running:
            cls()
            title = '\ Inventory /'
            bar = int(((79 - len(title)) / 2)) * '='
            print('{0}{1}{0}\n\n'.format(bar, title))
            print(79*'-')
            print('  Your Inventory              Capacity: 586')
            print(79*'-')

            try:
                for line in range(0 + mod_x, 12 + mod_x):
                    print(all_inv[line])  # >>> should indicate selected item.
            except IndexError:
                pass

            print(79*'-')
            print('[w]: Up, [s]: Down, [x]:Exit, [space]: Use/Equip')
            print(79*'-', '\n')
            print(79*'=')
            new_input = msvcrt_input()
            # new_input = input() # Kept in case msvcrt_input stops working.
            if new_input == 'w':
                mod_x -= 1
            elif new_input == 's':
                mod_x += 1
            elif new_input == 'x':
                running = False


def test_inventory_menu():
    inv = Inventory()

    # Make items to Display.
    i1 = Item()
    i1.name = 'Relic'
    i1.value = 24
    i1.weight = 1

    i2 = Weapon()
    i2.name = 'Iron Sword'
    i2.value = 143
    i2.weight = 8
    i2.health = 100
    i2.damage = 10

    i3 = Armour()
    i3.name = 'Steel Helmet'

    i4 = Consumable()
    i4.name = 'Green Apple'

    i5 = Note()
    i5.name = 'Letter of Hope'

    i6 = Key()
    i6.name = 'Rusty Iron Key'

    # Add test items to inventory.
    inv.add_item(i1)
    inv.add_item(i1)
    inv.add_item(i2)
    inv.add_item(i2)
    inv.add_item(i2)
    inv.add_item(i2)
    inv.add_item(i3)
    inv.add_item(i3)
    inv.add_item(i3)
    inv.add_item(i4)
    inv.add_item(i4)
    inv.add_item(i5)
    inv.add_item(i6)
    inv.add_item(i6)
    inv.add_item(i6)

    inv.show_inv()

# test_inventory_menu()
