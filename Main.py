##import os
##import time
##import socket
##import platform
##
##opSys = platform.system()
##
##if opSys == 'Windows':
##    print('Windows')
##    os.system('pause')
##    
##elif opSys == 'Darwin':
##    print('Mac')
##    read -n1 -r -p "Press any key to continue..." key
##
##elif opSys == 'Linux':
##    print('Linux')
##    
##else:
##    print('You are Lucky')

import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('0.0.0.0', 8080))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ''

    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print(from_client)

        conn.send("I am SERVER\n")

    conn.close()
    print("CLIENT DISCONNECTED")

