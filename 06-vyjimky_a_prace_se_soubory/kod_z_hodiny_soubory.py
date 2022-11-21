#raise ValueError('Vyhodim vyjimku')

# try:
#     i = 1/0
# except ZeroDivisionError:
#     print('Deleni nulou')
# except ValueError:
#     print('Chybne')
# finally:
#     print('Konec')

import os
import sys

with open(os.path.join(sys.path[0], 'my_file2.txt'), encoding='utf8', mode='a') as f:
    # print(f.read())
    # print(f.readlines())
    # for line in f.readlines():
    #    print(line.rstrip().lstrip())
    f.write('Zlín (Town, Zlín)\n')
