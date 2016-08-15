class Stuff:
    def __init__(self):
        return

    @staticmethod
    def print_logo():
        print '''
       ____           _
 _ __ |  _ \ ___  ___| |_ ___  _ __ ___
| '_ \| |_) / _ \/ __| __/ _ \| '__/ _ \\
| |_) |  _ <  __/\__ \ || (_) | | |  __/
| .__/|_| \_\___||___/\__\___/|_|  \___|
|_|
        '''


class NotAFolder(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NotAFile(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
