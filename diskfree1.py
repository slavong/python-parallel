#!/usr/bin/env python3.6

import subprocess

ret = subprocess.run(["df", "-h", "/home"])  
print(ret)  
