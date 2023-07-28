'''
                                                    Pip Libraries Uninstaller
    
    This is the main file of the script, the one that will uninstall the libraries.

    Author: Zourethe
    Date: July, 17, 2023
'''

# Imports.
from os import popen

# Variables.
modules_list = popen('pip freeze')
data = modules_list.read().split('\n')
data.remove('')
data_len = len(data)

# Uninstall loop.
for x in range(data_len):
    log = popen('pip uninstall {} -y'.format(data[x]))
    output = log.read()
    print(output)
