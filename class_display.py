from class_level import *


class Display:
    def __init__(self, level):
        self.level = level
        self.resolution_x = 79
        self.resolution_y = 60
        self.map_x = 41     # Standards 23, 29, 41, 45
        self.map_y = 19     # Standards 15, 17, 19, 23
        self.map_margin = 2
        self.sidebar_size_x = self.resolution_x - (self.map_x + ((self.map_margin * 2) + 2))
        self.sidebar = []
        self.grid = []

    def build_topbar(self):
        self.grid.append(self.resolution_x * '=')
        self.grid.append('Silence fills the spaces between each distant footstep')
        self.grid.append('')
        self.grid.append(self.resolution_x * '_')
        self.grid.append('')

    def update_sidebar(self):
        self.sidebar = []
        player = self.level.entities[0]
        
        self.sidebar.append(' Location: {0}'.format(self.level.name))
        self.sidebar.append(' Area Level: 1')
        self.sidebar.append(' Time: 06:49')
        self.sidebar.append(self.sidebar_size_x * '_')
        self.sidebar.append('')
        
        obj = None
        if player.facing == 'north':
            obj = self.level.grid[player.pos_y - 1][player.pos_x]
        elif player.facing == 'west':
            obj = self.level.grid[player.pos_y][player.pos_x - 1]
        elif player.facing == 'south':
            obj = self.level.grid[player.pos_y + 1][player.pos_x]
        elif player.facing == 'east':
            obj = self.level.grid[player.pos_y][player.pos_x + 1]
            
        # Appending relevant info of obj to the sidebar based on the obj TYPE.
        if obj in self.level.scene_chars:
            if obj == 'T':
                self.sidebar.append(' {0:<16}'.format('Birch Tree'))
                self.sidebar.append(' {0:<16} [ {1:>3} ]'.format('  Resource: ', 'Logs'))
                self.sidebar.append('')
                self.sidebar.append(' Required Tool:')
                self.sidebar.append('   Hatchet')
            elif obj == 'w':
                self.sidebar.append(' {0:<16}'.format('Water'))
            else:
                self.sidebar.append(' {0}'.format(obj))
        elif obj.TYPE == 'Humanoid':
            self.sidebar.append(' {0:<16} Level: {1}'.format(obj.name, obj.xp_level))
            self.sidebar.append(' {0:<16} [ {1:>3} ]'.format('  Health: ', obj.health))
            self.sidebar.append(' {0:<16} [ {1:>3} ]'.format('  Stamin: ', obj.stamina))
            self.sidebar.append(' {0:<16} [ {1:>3} ]'.format('  Damage:', obj.damage))
            self.sidebar.append('')
            self.sidebar.append(' Weapon:')
            self.sidebar.append('   Huge Wooden Club')
        elif obj.TYPE == 'Container':
            self.sidebar.append(' {0:<16} Lock: {1}'.format(obj.name, obj.keyLevel))
            self.sidebar.append(' {0:<16} [ {1:>3} ]'.format('  Capacity: ', 'obj.inventory._capacity'))
            self.sidebar.append('')
            self.sidebar.append(' Contents:')
            self.sidebar.append('   random_level_1_food')
            self.sidebar.append('   random_level_1_food')
            self.sidebar.append('   random_level_1_tools')

    def build_world_view(self):
        buff_y = int(self.map_y / 2)
        buff_x = int(self.map_x / 2)
        for pass1 in range(self.map_y):
            # world map
            row = '|{0}'.format(self.map_margin * ' ')
            for pass2 in range(self.map_x):
                y = (self.level.entities[0].pos_y - buff_y) + pass1
                x = (self.level.entities[0].pos_x - buff_x) + pass2
                if y < 0 or x < 0:
                    row += self.level.void_char
                else:
                    try:
                        if self.level.grid[y][x] in self.level.scene_chars:
                            row += str(self.level.grid[y][x])
                        else:
                            row += str(self.level.grid[y][x].key)
                    except IndexError:
                        row += self.level.void_char
            row += self.map_margin * ' '
            # sidebar
            if len(self.sidebar) > pass1:
                row += '|{0}'.format(self.sidebar[pass1])
            else:
                row += '|'
            self.grid.append(row)

    def build_status_bar(self):
        player = self.level.entities[0]  # Or whatever entity happens to be the player.
        self.grid.append(self.resolution_x * '-')
        self.grid.append('  Health:   [ {0:>3} ] | Level:    [ {1:>3} ] | Name:     {2} '.format(player.health, player.xp_level, player.name))
        self.grid.append('  Stamina:  [ {0:>3} ] | Strength: [ {1:>3} ] | Facing:   {2} '.format(player.stamina, player.strength, player.facing))
        self.grid.append('  Damage:   [ {0:>3} ] | Armour:   [ {1:>3} ] | Weapon:   {2} '.format(player.damage, player.protection, 'Nasphapipaphession Sword'))
        self.grid.append(self.resolution_x * '=')

    def d(self):  # The current display cycle for after every player movement
        self.grid = []
        self.level.update_entities()
        self.build_topbar()
        self.update_sidebar()
        self.build_world_view()
        self.build_status_bar()

        cls()
        for row in range(len(self.grid)):
            print(self.grid[row])
