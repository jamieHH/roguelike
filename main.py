from class_display import *


def main_menu():
    cls()
    title = '\ ROGUELIKE /'
    bar = int(((79 - len(title)) / 2)) * '='
    print('{0}{1}{0}\n\n'.format(bar, title))
    print(60 * '-')
    print('Main Menu')
    print(60 * '-', '\n')
    print('{0:<30}{1:<30}'.format('[0]: Start New Game', '[3]: Settings'))
    print('{0:<30}{1:<30}'.format('[1]: Load Saved Game', '[4]: Help'))
    print('{0:<30}{1:<30}'.format('[2]: Open Saves File', '[5]: Exit\n'))
    print(60 * '-')
    print('[Number keys]: Make selection')
    print(60 * '-', '\n\n', )
    print(79 * '=')
    print('Credit: Jamie Hatswell-Hough - 2015', '\n\n')


def menu_select(text, options):
    selection = input(text)
    if selection not in options:
        input('Selection invalid! [Enter]: Try again.\n')
    return selection


def get_new_game_world_files(region_directory):
    world_files = get_file_names(region_directory)
    return world_files


def new_game_menu(world_files):
    cls()
    title = '\ Start New Game /'
    bar = int(((79 - len(title)) / 2)) * '='
    print('{0}{1}{0}\n\n'.format(bar, title))
    print(60 * '-')
    print('Select a world:')
    print(60 * '-', '\n')
    # files = get_file_names('Regions/Test World')
    for i in range(len(world_files)):
        print('[{0:>2}]: {1:<20}'.format(i + 1, world_files[i]))
    print()
    print(60 * '-')
    print('[x]: Back')
    print(60 * '-', '\n\n')
    print(79 * '=', '\n')
    

def show_saves():
    cls()
    title = '\ Load Saved Game /'
    bar = int(((79 - len(title)) / 2)) * '='
    print('{0}{1}{0}\n'.format(bar, title))
    print(60 * '-', '\n')
    files = get_file_names()
    for save in range(len(files)):
        print('[{0:>2}]: {1:<20} (Saved: 01/08/16) (Game Time: 000 Days) '.format(save, files[save]))
        print('      (Location: Test World) (Player: Semi-Paagh) \n')
        
    print(60 * '-', '\n')
    print(79 * '=', '\n')

    i = input('E[x]it: ')


def load_game(file_name):
    # World/Region file is passed in to be interpreted.
    # Needs to access the assets for monsters, characters, items, inventories.
    # Will need to load all levels/worlds, all entities in each separate world.
    # All the world links.

    input('[enter]: Continue')
    pass


def run_game(world):
    # The game files will need to be loaded here.
    
    d = Display(world)
    asking = True
    while asking:
        d.d()
        new_input = msvcrt_input()
        # new_input = input('Control: ')  # Kept in case msvcrt_input stops working.
        if new_input != 'M':
            world.entities[0].get_key_input(new_input, world)
        else:
            asking = False

# main
running = True
while running:
    main_menu()
    selection = menu_select('Choose: ', ['0', '1', '2', '3', '4', '5'])
    
    if selection == '0':
        world_files = get_new_game_world_files('Regions/Test World')
        new_game_menu(world_files)
        worlds = []
        choices = []

        for i in range(len(world_files)):
            worlds.append('{0}{1}'.format('Regions/Test World/', world_files[i]))
            choices.append(str(i + 1))
        choices.append('x')

        worldChoice = menu_select('Choose: ', choices)

        if (worldChoice != 'x') and (worldChoice in choices):
            world = Level()
            world.read_level(worlds[int(worldChoice) - 1])
            run_game(world)

    elif selection == '1':
        pass
    
    elif selection == '2':
        show_saves()
        
    elif selection == '3':
        pass
        
    elif selection == '4':
        pass
    
    elif selection == '5':
        i = input('Do you want to quit? (y/n) ').lower()
        if i == 'y':
            running = False
            print('Quitting...')

print('The world dies without your part.')
