'''
DOCSTRING: Just run this file to install all the requirements to use this OS.
NB: You must have Python 3.x installed in your device.
'''

from sys import platform
import os

if platform.lower() == 'linux':
    try:
        os.system('sudo apt install python3-pip')
        print('\npip3 installed.\n\n')
        os.system('pip3 install colorama')
        print('\ncolorama installed.\n\n')
        os.system('pip3 install pymongo')
        print('\npymongo installed.\n\n')
    except:
        print('\nThis pogram is no longer compatible with your device.')
        print('Contact the developers for more info.\n')

elif platform.lower() == 'darwin':
    try:
        os.system('sudo python3 get-pip.py')
        print('\npip3 installed.\n\n')
        os.system('pip3 install colorama')
        print('\ncolorama installed.\n\n')
        os.system('pip3 install pymongo')
        print('\npymongo installed.\n\n')

    except:
        print('\nThis pogram is no longer compatible with your device.')
        print('Contact the developers for more info.\n')

elif platform.lower() == 'windows':
    try:
        os.system('sudo python3 get-pip.py')
        print('\npip3 installed.\n\n')
        os.system('pip3 install colorama')
        print('\ncolorama installed.\n\n')
        os.system('pip3 install pymongo')
        print('\npymongo installed.\n\n')
    except:
        print('\nThis pogram is no longer compatible with your device.')
        print('Contact the developers for more info.\n')
