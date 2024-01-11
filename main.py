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

# Terminal interface.
print('\033[32m{}\33[0m'.format('                       Pip Libraries Uninstaller'))
print('')
print('This is a pip libraries uninstaller, it uninstalls all libraries that appears in\nthe \033[31mpip freeze\033[0m list. To use it just press \033[31m1\033[0m and hit \033[31mEnter\033[0m.1')
print('')
print(' 1 - Start.')
print(' 0 - Exit.')
print('')
t_input = int(input('Command: '))

# Start or exit condition.
while True:
    if t_input == 1:
        # Uninstall loop.
        for x in range(data_len):
            log = popen('pip uninstall {} -y'.format(data[x]))
            output = log.read()
            print(output)
        break
    elif t_input == 0:
        break
    else:
        print('\033[31mIncorrect number\033[0m')
        t_input = int(input('Command: '))
