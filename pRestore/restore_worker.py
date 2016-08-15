from threading import Thread
import os


class Worker(Thread):

    def __init__(self, file_path, verbose):
        Thread.__init__(self)
        self.done = False
        self.verbose = verbose
        self.path = file_path
        self.file = open(self.path, 'r')

    def run(self):
        content = self.file.read().split('\n')
        for line in content:
            explode = line.split(':::')
            if len(explode) < 2:
                continue
            permissions = explode[1]
            owner_p = permissions[0:3].replace('-', '')
            group_p = permissions[3:6].replace('-', '')
            other_p = permissions[6:9].replace('-', '')
            owner = explode[2]
            group = explode[3]
            name = explode[-1]
            query1 = 'chmod u=%s,g=%s,o=%s %s;' % (owner_p, group_p, other_p, name)
            query2 = 'chown %s:%s %s' % (owner, group, name)
            if os.path.exists(name):
                os.system(query1)
                os.system(query2)
                if self.verbose:
                    print 'Setting permissions for %s (u=%s,g=%s,o=%s, %s:%s)' % (name, owner_p, group_p, other_p, owner, group)
        self.done = True

