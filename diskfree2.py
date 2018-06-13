#!/usr/bin/env python3.6

import subprocess

# Call the command
output = subprocess.run(["df", "-h", "/home"], stdout=subprocess.PIPE)

# Read the return code and the output data
print ("Return code: %i" % output.returncode)  
print ("Output data: %s" % output.stdout)  
