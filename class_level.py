from class_humanoid import *


class Level:
    """Record of individual level data"""
    
    def __init__(self):
        self.name = 'World'
        self.size_x = 0
        self.size_y = 0
        self.area_level = 1
        self.grid = []
        self.scenery = []
        self.scene_chars = []  # To solve conflicts with scenery and entities
        self.void_char = ' '
        self.entities = []

    def display_grid(self):
        self.update_entities()
        for pass1 in range(len(self.grid)):
            for pass2 in range(len(self.grid[pass1])):
                if self.grid[pass1][pass2] in self.scene_chars:
                    print(self.grid[pass1][pass2], end='')
                else:
                    print(self.grid[pass1][pass2].key, end='')
            print()
        pass
        
# ---------------------------------------------------------------- Reading Level
    def read_level(self, file_name):
        cls()
        file_lines = get_file_lines(file_name)

        # Reads the x and y size space that represents the level scenery.
        self.name = file_lines[0]
        temp = file_lines[1][0] + file_lines[1][1] + file_lines[1][2]
        self.size_x = int(temp)
        temp = file_lines[1][4] + file_lines[1][5] + file_lines[1][6]
        self.size_y = int(temp)

        # Loop below reads the scenery of the level from the file.
        self.scenery = []
        self.void_char = file_lines[2][0]
        for Row in range(2, self.size_y + 2):  # read indexes are shifted.
            x = []
            for Column in range(self.size_x):
                x.append(file_lines[Row][Column])
            self.scenery.append(x)

        self.grid = self.scenery      

        # This loop populates .scene_chars, listing what chars are scenery only.
        for y in range(len(self.scenery)):
            
            for x in range(len(self.scenery[y])):
                if self.scenery[y][x] not in self.scene_chars:
                    self.scene_chars.append(self.scenery[y][x])
        
        # This block reads and decodes data used to add entities to the level.
        print('\nRunning Level Decoder For: {0}...\n'.format(file_name))
        first_entity = 2 + self.size_y  # Line containing the first entity data.
        for i in range(int((len(file_lines) - first_entity) / 2)):
            print('|Entities Left to Decode:', int((len(file_lines) - first_entity) / 2))
            print('|--------------------')
            try:
                data = file_lines[first_entity + 1]
                x = str(data[0] + data[1] + data[2])
                y = str(data[4] + data[5] + data[6])
                inv = 'defaultInv'  # should be text file containing inv data
                
                # These queries check what type of entity to apply the data to.
                # Humanoid object.
                if file_lines[first_entity][0] == 'H':
                    entity = Humanoid(int(x), int(y), inv)
                    entity.read_attributes(file_lines[first_entity])
                    print('|--------------------')
                    print('|Appending Humanoid:', file_lines[first_entity], 'as', entity.name)
                    print('|X:', entity.pos_x, '\n|Y:', entity.pos_y, '\n|INVY:', entity.inventory, '\n|')
                # Container object.
                elif file_lines[first_entity][0] == 'C':
                    entity = Container(int(x), int(y), inv)
                    entity.read_attributes(file_lines[first_entity])
                    print('|--------------------')
                    print('|Appending Container:', file_lines[first_entity], 'as', entity.name)
                    print('|X:', entity.pos_x, '\n|Y:', entity.pos_y, '\n|INVY:', entity.inventory, '\n|')
                else:
                    entity = None
                
                self.add_entity(entity)  # Append the entity to the world.
                first_entity += 2  # Moves the reading head to the next entity.
                
            except IndexError:
                print('|Error: No entities preasent!')

        print('|Level File: "{0}" Processed!\n'.format(file_name))
        print('Level Decoder Stopped!\n')
        input('[Enter]: Continue \n')
        

# ------------------------------------------------------------------------------
    def map_scenery(self):  # ## FUCKING CUNT OF A SHITSTAINED HEAP OF BULLFUCK DEGENERATE FUCK BAGS!!!
        self.grid = []
        # self.grid = self.scenery  # TODO: <<< WHY DON'T THIS FUCKING WORK!!!
        for row in range(len(self.scenery)):
            new_row = []
            for column in range(len(self.scenery[row])):
                new_row.append(self.scenery[row][column])
            self.grid.append(new_row)

    def update_entities(self):
        # TODO: Should reset the grid to the scenery, then updates the positions of the grids entities.
        self.map_scenery()  # TODO: WHY THE FUCK don't self.grid = self.scenery work!?!

        for ent in range(len(self.entities)):
            self.grid[self.entities[ent].pos_y][self.entities[ent].pos_x] = self.entities[ent]

    def add_entity(self, entity):
        self.entities.append(entity)
    

# main
# w = Level()#
# w.read_level('Test World/CaveWorld.txt')
