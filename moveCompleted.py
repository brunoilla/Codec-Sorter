#!/usr/bin/env python3
import os
import shutil

DIRS = r'/mnt/user/Downloads/completed'
PreConversion = r'/mnt/user/Downloads/PreConversion'
Converted = r'/mnt/user/Plex/Converted'

for root, subdirs, files in os.walk(DIRS):
    print('root', root)
    print('subdirs', subdirs)
    print('files', files)

    for file in files:
        # If the file is encoded in H.265 it can go to the Organize directory.
        path = os.path.join(root, file)

        # Since I use this NAS with a MacOS machine I get unwanted .DS_Store files that can just be ignored
        if 'DS' in file:
            continue

        # All the files that already have the desired codec will be moved to the desired directory
        if '265' in file or 'HVENC' in file:
            shutil.move(path, Converted)
        else:
            shutil.move(path, PreConversion)
