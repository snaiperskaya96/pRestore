import os
import tarfile
from Queue import Queue
from threading import Thread
from time import time
from stuff import NotAFolder


class Writer(Thread):
    def __init__(self, out):
        Thread.__init__(self)
        self.chunk_size = 1024 * 1024 * 10 - 1  # 10MB
        self.queue = Queue()
        self.got_to_run = True
        self.tar = None
        self.index = 1
        self.file = None
        self.bytes_count = 0
        self.file_list = [1]
        self.queue_counter = 0
        if not os.path.exists(out):
            raise NotAFolder(out + ' is not a valid folder')
        self.out = out
        if self.out[-1] != '/':
            self.out += '/'

    def add(self, f):
        self.queue.put(f)

    def run(self):
        self.file = open('/tmp/prestore_' + str(self.index), 'w')
        while True:
            if not self.got_to_run and self.queue.empty():
                break
            if self.queue.empty():
                continue
            f = self.queue.get()
            if f.permissions != '':
                line = "%s:::%s:::%s:::%s:::%s\n" % (f.first_char, f.permissions, f.owner, f.group, f.path)
                self.bytes_count += len(line)
                self.file.write(line)
                if self.bytes_count >= self.chunk_size:
                    self.index += 1
                    self.file.close()
                    self.file_list.append(self.index)
                    print 'Chunk %s closed.' % str(self.index - 1)
                    self.file = open('/tmp/prestore_' + str(self.index), 'w')
                    self.bytes_count = 0
        self.file.close()
        self.tar = tarfile.open(self.out + str(time()) + '_prestore.list', 'w:bz2')
        for f in self.file_list:
            self.tar.add('/tmp/prestore_' + str(f), arcname='prestore_' + str(f))
        self.tar.close()
        os.remove('/tmp/prestore_' + str(self.index))

    def stop(self):
        self.got_to_run = False
