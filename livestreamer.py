#!/usr/bin/env python3

import subprocess
import os
import sys

def tryexec(paths, args):
    for path in paths:
        basename = os.path.basename(path)
        try:
            os.execlp(path, basename, *args)
        except FileNotFoundError:
            pass
    raise FileNotFoundError

def vlc(arg):
    tryexec(['vlc', r'C:\Program Files (x86)\VideoLAN\VLC\vlc.exe'], 
        ['--', arg]
    )

url = sys.argv[1][15:] 

print (url)

subprocess.call(['/usr/bin/livestreamer', url, 'source'])
