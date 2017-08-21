class OptionMenu:
    def __init__(self, title, header, footer, options):
        self.resolution_x = 79
        self.resolution_y = 29
        self.title = title
        self.heading = header
        self.footer = footer
        self.options = options

    def build_menu(self):
        y_count = self.resolution_y
        
        bar = int(((self.resolution_x - len(self.title)) / 2)) * '='
        print('{0}{1}{0}\n\n'.format(bar, self.title))

        print(60 * '-')
        print(self.heading)
        print(60 * '-')

        print()
        for q in range(len(self.options)):
            print('[{0:>2}]: {1:<20}'.format(q + 1, self.options[q]))
            y_count -= 1

        # for x in range(y_count - 14):
        #     print()
        print()

        print(60 * '-')
        print(self.footer)
        print(60 * '-', '\n\n')

        print(self.resolution_x * '=')


class ScrollingMenu:
    def __init__(self, title, header, footer, columns, sections, data):
        self.resolution_x = 79
        self.resolution_y = 29
        self.title = title
        self.heading = header
        self.footer = footer

        self.columns = columns
        self.sections = sections
        self.data = data

    def build_menu(self):
        y_count = self.resolution_y

        bar = int(((self.resolution_x - len(self.title)) / 2)) * '='
        print('{0}{1}{0}\n\n'.format(bar, self.title))

        print(60 * '-')
        print(self.heading)
        print(60 * '-')

        # table = []  # This code was taken from class_inventory. This should be made dynamic.
        # table.append('|--------------------------------------------------------|')
        # table.append('|Weapons                      |Value|Weight|Health|Damage|')
        # for i in range(len(self._weapons)):
        #     item = self._weapons[i]
        #     table.append(
        #         '|{0}: {1:<24}|{2:>5}|{3:>6}|{4:>6}|{5:>6}|'.format(
        #             select, item.name, item.value, item.weight, item.health, item.damage
        #         )
        #     )

        print(60 * '-')
        print(self.footer)
        print(60 * '-', '\n\n')

        print(self.resolution_x * '=')


def test_option_menu():
    m = OptionMenu('Test Menu', 'Heading', 'Footer', ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'])
    m.build_menu()
    input()


test_option_menu()
