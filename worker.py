from threading import Thread
import subprocess
from file import File


class Worker(Thread):
    def __init__(self, directory, parent):
        Thread.__init__(self)
        self.directory = directory
        self.parent = parent

    def run(self):
        process = subprocess.Popen(['ls', '-lah', self.directory], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.communicate()[0].split('\n')
        if process.returncode != 0:
            self.parent.on_thread_finished(self)
        else:
            index = 0
            for line in output:
                if index > 2:
                    f = File(line)
                    f.path = self.directory + f.name
                    self.parent.write(f)
                    if f.is_directory:
                        self.parent.add_to_queue(self.directory + f.name)
                index += 1
        self.parent.on_thread_finished(self)
