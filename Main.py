import os
import time
import socket
import platform

opSys = platform.system()

if opSys == 'Windows':
    print('Windows')
    os.system('pause')
    
elif opSys == 'Darwin':
    print('Mac')
    read -n1 -r -p "Press any key to continue..." key

elif opSys == 'Linux':
    print('Linux')
    
else:
    print('You are Lucky')

