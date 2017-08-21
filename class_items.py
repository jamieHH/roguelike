from functions import *


class Item:
    TYPE = 'None'

    def __init__(self):
        self.name = "DefaultName"
        self.level = 1
        self.value = 0
        self.weight = 0
        
    # is there a better way to read item attributes without rewriting the code
    # should read_attribs be a global function instead of a private method?
    # yes, yes it should...
    
    def read_attributes(self, file_name):
        file_name = 'Assets/Items/{0}'.format(file_name)
        valid_attribs = ['NAME', 'TYPE', 'LEVL', 'VLUE', 'WGHT']
        f = open(file_name, 'r')
        print('Reading Item file:', file_name)

        # This loop decodes each attribute and value line by line in the file.
        for line in f:
            reading = True
            try:
                attrib = line[0] + line[1] + line[2] + line[3]
                print(attrib)
            except IndexError:
                print('Error: Line With No Named Attribute.')
                reading = False

            # This loop reads the value of valid attributes.
            if reading and (attrib in valid_attribs):
                value = []
                for i in range(5, len(line) - 1):
                    value.append(line[i])  # Reads value excluding \n.
                value = ''.join(value)  # Stringifes value.
                print(' ', value)
                
                # Assigning values to the attribute addressed in the read loop.
                if attrib == 'NAME':
                    self.name = value
                # TYPE is automatically assigned to Container for all containers.
                elif attrib == 'LEVL':
                    self.level = value
                elif attrib == 'VLUE':
                    self.value = value
                elif attrib == 'WGHT':
                    self.weight = int(value)
                # Last value gets ignored without returning at the end.
                # Make sure each txt file has an empty line at the end.
                else:
                    print('Attribute Not Assigned.')
            
            else:
                if not reading:
                    print('Attribute Discarded.')
                else:
                    print('Error: Unrecognised Attribute.')
        print()
        print('File: "{0}" Processed!'.format(file_name))
        print('----------')
        print()
        f.close()
        

class Weapon(Item):
    TYPE = 'Weapon'

    def __init__(self):
        super().__init__()
        self.damage = 0
        self.health = 100


class Armour(Item):
    TYPE = 'Armour'

    def __init__(self):
        super().__init__()
        self._defence = 0
        self.health = 100
        

class Consumable(Item):
    TYPE = 'Consumable'

    def __init__(self):
        super().__init__()
        self._effect = []  # List of effects
        # Think about effect, magnitude, every (x) turns, for (x) turns...
        # Or instant effect.

        # Create Spell/effect text file reader.


class Note(Item):
    TYPE = 'Note'

    def __init__(self):
        super().__init__()
        self._headers = []  # List used in case of multiple chapters/titles.
        self._text = []  # Text can be split up to match the header index.
        # Create Note text file reader.


class Key(Item):
    TYPE = 'Key'

    def __init__(self):
        super().__init__()
        self._locks = []  # List of named doors/containers the key can open.
        self._durability = 000  # Durability for lock picks, 000 = invulnerable
