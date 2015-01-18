#!/usr/bin/env python3

import subprocess
import sys

url = sys.argv[1][15:]
subprocess.call(['/usr/bin/livestreamer', url, 'source'])
