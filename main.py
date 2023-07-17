'''
                            Pip Libraries Uninstaller
    
    This is the main file of the script, the one that will uninstall the libraries.

    Author: Zourethe
    Date: July, 17, 2023
'''

# Libraries imports.
from os import popen

# Variables definition.
modules_list = popen('pip freeze')
data = modules_list.read().split('\n')
data.remove('')
data_len = len(data)

# Loop to uninstall each library.
for x in range(data_len):
    log = popen('pip uninstall {} -y'.format(data[x]))
    output = log.read()
    print(output)
