import re


class File:
    def __init__(self, line):
        self.permissions = ''
        self.first_char = ''
        self.is_file = False
        self.is_link = False
        self.is_directory = False
        self.is_empty = False
        self.directories = 0
        self.owner = ''
        self.group = ''
        self.size = ''
        self.last_edit = ''
        self.name = ''
        self.path = ''
        self.elaborate(line)

    def elaborate(self, line):
        regex = '([dl-]{1})([rwxt\-]{9}[\@\+]?) *([0-9]*) *([a-zA-Z0-9\-\_]*) *([a-zA-Z0-9\-\_]*) *([a-zA-Z0-9\.\,]*) *([A-Za-z]{3}) *([0-9]{1,2}) *([0-9:]*) *([a-zA-Z0-9\.\-\_ \> /]*)'
        result = re.search(regex, line)

        if result is None:
            return

        if result.group(1) == 'd':
            self.is_directory = True
        elif result.group(1) == 'l':
            self.is_link = True
        elif result.group(1) == '-':
            self.is_file = True

        self.first_char = result.group(1)
        self.permissions = result.group(2)
        self.directories = result.group(3)
        self.owner = result.group(4)
        self.group = result.group(5)
        self.size = result.group(6)
        self.last_edit = result.group(7) + result.group(8)
        self.name = result.group(10)

        self.is_empty = int(self.directories) == 0
