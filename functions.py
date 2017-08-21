import os
import msvcrt


def cls():  # Used to wipe the command prompt after each Display tick.
    os.system('cls' if os.name == 'nt' else 'clear')


def msvcrt_input():
    new_input = str(msvcrt.getch())
    output = new_input[-2]  # Only listing that seams to work: [-2].
    if output == 'f':  # 'f' apparently represents no input in idle.
        output = input('Msvcrt error! Reverting to input: ')
    return output


def get_file_names(directory=os.getcwd()):
    # Return a list of file names in the directory.
    cwd = directory
    files_names = os.listdir(cwd)
    return files_names


def get_file_type(file):
    # Return the type of file being read.
    # file_name WITHOUT directory!
    if file[0] == 'C':
        file_type = 'Container'
    elif file[0] == 'H':
        file_type = 'Humanoid'
    elif file[0] == 'V':
        file_type = 'Inventory'
    elif file[0] == 'I':
        file_type = 'Item'
    elif file[0] == 'W':
        file_type = 'Weapon'
    elif file[0] == 'A':
        file_type = 'Armour'
    elif file[0] == 'E':  # For Edible
        file_type = 'Consumable'
    elif file[0] == 'N':
        file_type = 'Note'
    elif file[0] == 'K':
        file_type = 'Key'
    else:
        file_type = None
    return file_type


def get_file_lines(file_name):
    # Return each line in a text file in a list.
    f = open(file_name, 'r')
    print('Reading Lines in File:', file_name)
    file_lines = []
    for line in f:
        row = []
        for count in range(len(line)):
            if line[count] != '\n':
                row.append(line[count])
        row = ''.join(row)  # Stringifies row
        file_lines.append(row)
    for count in range(len(file_lines)):
        print(file_lines[count])
    f.close()
    return file_lines


def get_file_attribs(file_name, file_type):
    # Read attributes and values from a txt file.
    log_dent = ''  # Indent to make the decode log more readable.
    if file_type in ['Humanoid', 'Container']:
        log_dent = '  '
    elif file_type == 'Inventory':
        log_dent = '    '
    elif file_type in ['Item', 'Weapon', 'Armour', 'Consumable', 'Note', 'Key']:
        log_dent = '      '

    attribs = []
    values = []
    f = open(file_name, 'r')
    print('{0}|Reading {1} File: {2}'.format(log_dent, file_type, file_name))

    # This loop decodes each attribute and value line by line in the file.
    for line in f:
        reading = True
        try:
            # Reading the 4 char long attrib reference.
            attrib = line[0] + line[1] + line[2] + line[3]
            print('{0}|{1}'.format(log_dent, attrib))
            attribs.append(attrib)

            # Reading the value of the attribute.
            value = []
            for i in range(5, len(line) - 1):
                value.append(line[i])  # Reads value excluding \n.
            value = ''.join(value)  # Stringifes value.
            print('{0}|  {1}'.format(log_dent, value))  #
            if value == 'i':
                print('{0}|  Value determined via parameter.'.format(log_dent))
            values.append(value)

        except IndexError:
            print('{0}|Error: Line With No Named Attribute.'.format(log_dent))
            reading = False
    f.close()

    # Return all the data using a 2D list.
    data = [attribs, values]
    return data
