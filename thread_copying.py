#!/usr/bin/env python
"""Copy all files and directories from source to backup directories using multiprocessing"""

import subprocess
import os
from multiprocessing import Pool

root='/home/user/user-name/'
dir_list = ['alpha','beta','delta','gamma','kappa','omega','sigma']


def copy(dir):
	src = root +'data/prod/' + dir
	dest = root +'data/prod_backup/'
	subprocess.call(["rsync", "-arq", src, dest])
	print ('Copying : ',dir)


if __name__ == "__main__":
	p = Pool(len(dir_list))
	p.map(copy, dir_list)
