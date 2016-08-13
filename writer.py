from threading import Thread
from Queue import Queue
from time import time
import os
import tarfile


class Writer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.chunk_size = 1024 * 1024 * 10 - 1  # 10MB
        self.queue = Queue()
        self.got_to_run = True
        self.tar = None # tarfile.open(str(time()) + '_prestore.list', 'w:bz2')
        self.index = 1
        self.file = open('/tmp/prestore_' + str(self.index), 'w')
        self.bytes_count = 0
        self.file_list = []

    def add(self, file):
        self.queue.put(file)

    def run(self):
        while self.got_to_run:
            file = self.queue.get()
            if file.permissions != '':
                line = "%s:::%s:::%s:::%s:::%s\n" % (file.first_char, file.permissions, file.owner, file.group, file.path)
                self.bytes_count += len(line)
                self.file.write(line)
                if self.bytes_count >= self.chunk_size:
                    self.file.close()
                    self.file_list.append(self.index)
                    # self.tar.add('/tmp/prestore_' + str(self.index))
                    # os.remove('/tmp/prestore_' + str(self.index))
                    print 'Chunk %s closed.' % str(self.index)
                    self.index += 1
                    self.file = open('/tmp/prestore_' + str(self.index), 'w')
                    self.bytes_count = 0
        self.file.close()
        self.tar = tarfile.open(str(time()) + '_prestore.list', 'w:bz2')
        for file in self.file_list:
            self.tar.add('/tmp/prestore_' + str(file))
        os.remove('/tmp/prestore_' + str(self.index))
