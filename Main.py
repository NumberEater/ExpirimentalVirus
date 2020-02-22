import os
import time
import socket
import platform

opSys = platform.system()

if opSys == 'Windows':
    print('...')
    os.system('pause')
    
elif opSys == 'Darwin':
    print('...')

elif opSys == 'Linux':
    print('OS NOT SUPPORTED; VIRUS ABORTED')
else:
    print('You are Lucky')
