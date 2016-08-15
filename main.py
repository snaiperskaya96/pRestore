import argparse
from pRestore.stuff import Stuff
from pRestore.backup import  Backup
from pRestore.restore import Restore

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
                    help='The maximum number of threads that will be used for making the backup or restoring permissions')
parser.add_argument('--verbose', dest='verbose', action='store_const', default=False, const=True,
                    help='Display more detailed information about what the script is doing')

arguments = parser.parse_args()

target = arguments.target[0]
backup = arguments.backup
restore = arguments.restore
out = arguments.out
threads = arguments.threads
verbose = arguments.verbose

if restore:
    Restore(target, threads, verbose)
else:
    Backup(target, out, threads, verbose)
