import subprocess
from threading import Thread

import file_handler


class Worker(Thread):
    def __init__(self, directory, parent):
        Thread.__init__(self)
        self.daemon = True
        self.directory = directory
        self.parent = parent
        self.done = False

    def run(self):
        process = subprocess.Popen(['ls', '-lah', self.directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.communicate()[0].split('\n')
        if process.returncode != 0:
            self.done = True
        else:
            self.send_to_file(output)
            for line in output[3:]:
                f = file_handler.File(line)
                if f.is_directory and not f.is_empty:
                    self.parent.add_to_queue(self.directory + f.name)
        self.done = True

    def send_to_file(self, output):
        if len(output) < 3:
            return
        first_file = file_handler.File(output[3])
        first_file.path = self.directory + first_file.name
        files = [first_file]
        should_use_wildcard = True
        permissions = first_file.permissions + first_file.owner + first_file.group
        for line in output[3:]:
            f = file_handler.File(line)
            f.path = self.directory + f.name
            if f.name == '':
                continue
            files.append(f)
            if permissions != f.permissions + f.owner + f.group:
                should_use_wildcard = False
        if should_use_wildcard:
            first_file.path = self.directory + '*'
            self.parent.write(first_file)
        else:
            for f in files:
                self.parent.write(f)
