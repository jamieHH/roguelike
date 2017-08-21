from class_inventory import *


class Humanoid:
    """Class to as in living entities"""

    TYPE = 'Humanoid'
    
    def __init__(self, pos_x=0, pos_y=0, inventory=0):
        self.name = 'undefinedChar'
        self.bio = '(Character Bio)'
        self.key = 'X'
        self.inventory = inventory  # Record of an inventory.
        self.facing = 'north'
        self.location = ''  # Name of the current world.
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.xp_level = 1
        self.health = 100
        self.stamina = 100
        self.strength = 0
        self.protection = 0
        self.damage = 0
        
# ----------------------------------------------------------- Reading Attributes
    def read_attributes(self, file, file_type='Humanoid'):
        file_name = ('Assets/Entities/{0}'.format(file))
        print('  |Processing {0} File: {1}'.format(file_type, file_name))

        file_type = get_file_type(file)
        data = get_file_attribs(file_name, file_type)  # ########################
        attrib = data[0]
        value = data[1]

        for i in range(len(attrib)):
            # Assigning values to the attribute addressed in the read loop.
            if attrib[i] == 'NAME':
                self.name = value[i]
            # TYPE is automaticaly assigned to Humanoid for all characters.
            elif attrib[i] == 'BIO ':
                self.bio = value[i]
            elif attrib[i] == 'KEY ':
                self.key = value[i]
            elif attrib[i] == 'FACE':
                self.facing = value[i]
            elif attrib[i] == 'INVY':
                self.inventory = value[i]
            elif attrib[i] == 'LOCA':
                self.location = value[i]
            # PosX and Y values ignored to allow parameter override.
            elif attrib[i] == 'LEVL':
                self.xp_level = int(value[i])
            elif attrib[i] == 'HLTH':
                self.health = int(value[i])
            elif attrib[i] == 'STAM':
                self.stamina = int(value[i])
            elif attrib[i] == 'SRTH':
                self.strength = int(value[i])
            elif attrib[i] == 'PROT':
                self.protection = int(value[i])
            elif attrib[i] == 'DAMG':
                self.damage = int(value[i])
            # Last value gets ignored without returning at the end.
            # Make sure each txt file has an empty line at the end.
            else:
                print('  |  --Unknown attribute assignment: {0}!--'.format(attrib[i]))  #
        
        print('  |File: "{0}" Processed!'.format(file_name))  #
    
# ---------------------------------------------------------------- new_input methods
    def get_key_input(self, new_input, world):
        # Does this need to refer back from the world, to entity back to world???
        if new_input in ['w', 'a', 's', 'd']:  # Walk
            self.make_move(world, new_input)
        elif new_input in ['W', 'A', 'S', 'D']:  # Sprint
            self.make_move(world, new_input.lower())
            self.make_move(world, new_input.lower())
        elif new_input == ' ':  # Activate object
            if self.facing == 'north':
                obj = world.grid[self.pos_y - 1][self.pos_x]
                self.activate(obj)
            if self.facing == 'west':
                obj = world.grid[self.pos_y][self.pos_x - 1]
                self.activate(obj)
            if self.facing == 'south':
                obj = world.grid[self.pos_y + 1][self.pos_x]
                self.activate(obj)
            if self.facing == 'east':
                obj = world.grid[self.pos_y][self.pos_x + 1]
                self.activate(obj)
        elif new_input == 'q':
            print('No inventory. ')
        else:
            print('Key not assigned. ')

    def activate(self, obj):
        try:
            obj_type = obj.TYPE
            # There must be a more efficient way to do this.
            if obj_type == 'Humanoid':
                # Start combat functions.
                print(obj_type)
            elif obj_type == 'Container':
                # Open containers inventory if its unlocked.
                print(obj_type)
            elif obj_type == 'Merchant':
                # Open the buy/sell menu.
                print(obj_type)
            elif obj_type == 'Resource':
                # check if you have the required tools, give player resource...
                print(obj_type)
            elif obj_type == 'Door':
                # Check if you have the key, open close door, change door icon.
                print(obj_type)
            elif obj_type == 'World changer':
                # Like a door. Check humanoids inventory for the key then change the level.
                print(obj_type)
        except AttributeError:
            print('No objects nearby. {0} '.format(obj))
        
    def change_direction(self, move):
        if move == 'w':
            self.facing = 'north'
        elif move == 'a':
            self.facing = 'west'
        elif move == 's':
            self.facing = 'south'
        elif move == 'd':
            self.facing = 'east'

    def check_valid_move(self, world, move):
        # Prevents objects out of bounds error.
        valid_move = True
        if move not in ['w', 'a', 's', 'd']:    
            valid_move = False
        elif ((move == 'w') and (self.pos_y == 0)) or ((move == 's') and (self.pos_y == world.size_y - 1)):
            valid_move = False
        elif ((move == 'a') and (self.pos_x == 0)) or ((move == 'd') and (self.pos_x == world.size_x - 1)):
            valid_move = False

        # Checks if the grid space before the player is walkable (' or .).
        floor = ["'", '.']  # TODO: pass valid floorspace from world if possible
        try: 
            if (world.grid[self.pos_y - 1][self.pos_x] not in floor) and (move == 'w'):
                valid_move = False
            elif (world.grid[self.pos_y + 1][self.pos_x] not in floor) and (move == 's'):
                valid_move = False
            elif (world.grid[self.pos_y][self.pos_x - 1] not in floor) and (move == 'a'):
                valid_move = False
            elif (world.grid[self.pos_y][self.pos_x + 1] not in floor) and (move == 'd'):
                valid_move = False
        except IndexError:
            # Exception Needed in case the space extends outside the grid bounds.
            valid_move = False
        return valid_move

    def make_move(self, world, move):  # This reefers from the level...
        # ...and then back to the character. This is inefficient!!!
        self.change_direction(move)
        if self.check_valid_move(world, move):
            if move == 'w':
                self.pos_y -= 1
            elif move == 'a':
                self.pos_x -= 1
            elif move == 's':
                self.pos_y += 1
            elif move == 'd':
                self.pos_x += 1
            else:
                print()
        else:
            print('Invalid move by {0}. Made after move {1} at X{2} Y{3}.'.format(self.key, move, self.pos_x, self.pos_y))


# For testing attrib reading.
# f = Humanoid(0, 0)
# f.read_attributes('deftChar.txt')
