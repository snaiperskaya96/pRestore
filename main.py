import argparse

from pRestore.backup import Backup
from pRestore.stuff import Stuff

Stuff.print_logo()

description = 'pRestore is a software used to make backup of file permissions and restore them in case of disaster'

parser = argparse.ArgumentParser(description=description)
parser.add_argument('target', metavar='D', type=str, nargs=1, help='Target directory/Restore file')
parser.add_argument('--backup', dest='backup', action='store_const', const=True, default=False,
                    help='Make a backup of the target directory')
parser.add_argument('--restore', dest='restore', action='store_const', const=True, default=False,
                    help='Restore permissions from the target backup file')
parser.add_argument('--out', help='Output directory where to store the backup', default='.')
parser.add_argument('--threads', default=10,
                    help='The maximum number of threads that will be used for making the backup')

arguments = parser.parse_args()

target = arguments.target[0]
backup = arguments.backup
restore = arguments.restore
out = arguments.out
threads = arguments.threads

if restore:
    pass
else:
    Backup(target, out, threads)
