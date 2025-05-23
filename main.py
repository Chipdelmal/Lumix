#!/usr/bin/env python3

import shutil as sht
from glob import glob
from os import path, makedirs
from time import ctime, strptime, strftime
# from tqdm import tqdm


(PTH_I, PTH_O) = (
    [
        path.join('/Volumes/LUMIX', 'DCIM/'),
        path.join('/Volumes/NIKON D3400', 'DCIM/'),
        path.join('/Volumes/K-1 II', 'DCIM')
    ],
    # path.join('/Volumes/Eunie/')
    path.join('/Volumes/Kai/Lumix')
)
MOVE = False
for pth_i in PTH_I:
    ###########################################################################
    # Get all folders and iterate over them
    ###########################################################################
    fldrs = glob(path.join(pth_i, '*'))
    for fldr in fldrs:
        #######################################################################
        # Get filenames and iterate over them
        #######################################################################
        fnames = glob(path.join(fldr, '*'))
        for fname in fnames:
            pntStr = "Moving" if MOVE else "Copying"
            print(f'\033[94m * {pntStr} {fname}\033[0m')
            ###################################################################
            # Get file extensions
            ###################################################################
            fext = path.splitext(fname)[-1][1:]
            ###################################################################
            # Get file datetime
            ###################################################################
            (cTime, mTime) = (
                strptime(ctime(path.getctime(fname))),
                strptime(ctime(path.getmtime(fname)))
            )
            ###################################################################
            # Create output folder
            ###################################################################
            fldrNme = strftime("%Y_%m_%d", cTime)
            fldrOut = path.join(PTH_O, fldrNme, fext)
            if not path.exists(fldrOut):
                makedirs(fldrOut)
            fnameOut = path.join(fldrOut, path.split(fname)[-1])
            ###################################################################
            # Move or Copy files
            ###################################################################
            if MOVE:
                sht.move(fname, fnameOut)
            else:
                sht.copy(fname, fnameOut)