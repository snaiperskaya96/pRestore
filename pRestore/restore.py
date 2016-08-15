import tarfile
import os
import time

from pRestore.restore_worker import Worker
from stuff import NotAFile


class Restore:

    def __init__(self, target, threads, verbose):
        self.target = target
        self.verbose = verbose
        self.now = time.time()
        self.extract_path = '/tmp/pRestore/%s' % str(self.now)
        self.extracted_files = []
        self.MAX_THREADS = threads
        if not os.path.isfile(target):
            raise NotAFile('%s is not a valid file' % target)
        self.threads = []
        self.open_backup()

    def open_backup(self):
        try:
            os.mkdir('/tmp/pRestore')
        except OSError:
            pass

        with tarfile.open(self.target, 'r:bz2') as backup:
            for member_info in backup.getmembers():
                self.extracted_files.append(member_info.name)
            os.mkdir(self.extract_path)
            backup.extractall(self.extract_path)

        while True:
            for thread in self.threads:
                if thread.done:
                    self.threads.remove(thread)
            if len(self.threads) >= self.MAX_THREADS:
                continue
            if len(self.extracted_files) == 0:
                break
            for f in self.extracted_files:
                thread = Worker(self.extract_path + '/%s' % f, self.verbose)
                self.threads.append(thread)
                self.extracted_files.remove(f)
                thread.start()

        for thread in self.threads:
            thread.join()
            os.remove(thread.path)

        os.rmdir(self.extract_path)

        print 'Done'


