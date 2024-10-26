#!/usr/bin/env python3

import shutil as sht
from glob import glob
from os import path, makedirs
from time import ctime, strptime, strftime
# from tqdm import tqdm


(PTH_I, PTH_O) = (
    path.join('/Volumes/LUMIX', 'DCIM/100_PANA'),
    # path.join('/Users/chipdelmal/Pictures/Lumix')
    path.join('/Volumes/Kai/Lumix')
)
MOVE = False
###############################################################################
# Get filenames and iterate over them
###############################################################################
fnames = glob(path.join(PTH_I, '*'))
for fname in fnames:
    print(f'\033[94m * Processing {fname}\033[0m')
    ###########################################################################
    # Get file extensions
    ###########################################################################
    fext = path.splitext(fname)[-1][1:]
    ###########################################################################
    # Get file datetime
    ###########################################################################
    (cTime, mTime) = (
        strptime(ctime(path.getctime(fname))),
        strptime(ctime(path.getmtime(fname)))
    )
    ###########################################################################
    # Create output folder
    ###########################################################################
    fldrNme = strftime("%Y_%m_%d", cTime)
    fldrOut = path.join(PTH_O, fldrNme, fext)
    if not path.exists(fldrOut):
        makedirs(fldrOut)
    fnameOut = path.join(fldrOut, path.split(fname)[-1])
    ###########################################################################
    # Move or Copy files
    ###########################################################################
    if MOVE:
        sht.move(fname, fnameOut)
    else:
        sht.copy(fname, fnameOut)