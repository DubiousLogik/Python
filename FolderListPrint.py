#! /usr/bin/env python

import os
parent_dir = 'C:/Users/rob_2.000/Music/Various artists'

for subdir, dirs, files in os.walk(parent_dir):
    for folder in dirs:
        print os.path.join(subdir, folder)
        with open('c:/temp/music4.txt', 'a') as f:
            f.write('\n' + os.path.join(subdir, folder))

# for subdir, dirs, files in os.walk(parent_dir):
#     for file in files:
#         print os.path.join(subdir, file)

# for subdir, dirs in os.walk(parent_dir):
#     for dir in dirs:
#         print os.path.join(subdir, dir)